from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from typing import Optional, List
from pathlib import Path
from datetime import datetime
import json
import asyncio
import subprocess

from astro.utils import load_config, load_dotenv_config
from astro.embedder import create_embedder
from astro.chroma_client import (
    get_chroma_client,
    query_collection,
    add_to_collection,
    create_collection,
    get_collection_documents,
    get_collection_type
)
from astro.schema_loader import SchemaDefinition,FieldDefinition

# ─── 初期化 ───
load_dotenv_config()
config = load_config()
embed_text = create_embedder(config)
astro = FastAPI(
    title=config.api_title,
    description=config.api_description,
    version=config.api_version,
    contact={
        "name": config.api_contact_name,
        "url": config.api_contact_url,
        "email": config.api_contact_email,
    },
    license_info={
        "name": "Apache2.0 License Copyright (c) 齋藤みつる ふさもふ統合思念体 HIPSTAR",
        "url": "https://github.com/HIPSTAR-IScompany/astro.quantaril.cloud/blob/main/LICENSE",
    },
    openapi_extra={
        "x-origin": {
            "name": "齋藤みつる",
            "organization": "HIPSTAR / ふさもふ統合思念体",
            "url": "https://github.com/HIPSTAR-IScompany/astro.quantaril.cloud",
            "comment": "このOpenAPI定義はフォールド構文Astroの正規バージョンに基づく"
        }
    }
)

def custom_openapi() -> dict:
    if astro.openapi_schema:
        return astro.openapi_schema
    openapi_schema = get_openapi(
        title=astro.title,
        version=astro.version,
        description=astro.description,
        routes=astro.routes,
    )
    openapi_schema.setdefault("components", {}).setdefault("securitySchemes", {})[
        "BearerAuth"
    ] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }
    astro.openapi_schema = openapi_schema
    return astro.openapi_schema

astro.openapi = custom_openapi
# Chromaクライアントは起動時に非同期で初期化する
chroma_client = None
chroma_process = None

@astro.on_event("startup")
async def startup_event() -> None:
    """アプリ起動時に Chroma クライアントを初期化する"""
    global chroma_client, chroma_process
    if config.chroma_bind:
        chroma_process = subprocess.Popen(
            [
                "chroma",
                "run",
                "--path",
                config.chroma_bind_store,
                "--host",
                config.chroma_host,
                "--port",
                str(config.chroma_port),
            ]
        )
        await asyncio.sleep(3)
    chroma_client = await get_chroma_client()

@astro.on_event("shutdown")
async def shutdown_event() -> None:
    global chroma_process
    if chroma_process is not None:
        chroma_process.terminate()
        chroma_process.wait()
SCHEMA_DIR = Path(config.schema_dir)
BEARER_DIR = Path(config.astro_api_key_dir)

security_scheme = HTTPBearer(
    bearerFormat="JWT",
    scheme_name="BearerAuth",
    auto_error=False,
)

# ────────────────────────────────
# APIキー検証ユーティリティ
# ────────────────────────────────
def validate_api_key(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(security_scheme),
) -> None:
    if config.astro_api_key_mode.lower() != "bearer":
        return
    if not credentials:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    token = credentials.credentials
    for path in BEARER_DIR.glob("*.json"):
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                continue

            records = data if isinstance(data, list) else [data]
            for record in records:
                if not isinstance(record, dict):
                    continue
                if record.get("key") == token:
                    deadline = record.get("ExpiryDeadline")
                    if deadline:
                        try:
                            expiry = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S %Z")
                            if datetime.now().astimezone() > expiry:
                                raise HTTPException(status_code=403, detail="API key expired")
                        except Exception:
                            raise HTTPException(status_code=500, detail="Invalid ExpiryDeadline format")
                    return
    raise HTTPException(status_code=403, detail="Invalid API key")

# ────────────────────────────────
# リクエストスキーマ
# ────────────────────────────────
class EmbedRequest(BaseModel):
    text: str
    collection: str  # スキーマファイル名 or 任意名
    metadata: Optional[dict] = None


class QueryRequest(BaseModel):
    query: str
    collection: str
    top_k: int = 3


class AddRequest(BaseModel):
    items: List[DocumentItem]
    collection: str


class CreateCollectionRequest(BaseModel):
    name: str
    schema_file: str  # スキーマ名（JSONファイル名）


# ────────────────────────────────
# APIエンドポイント
# ────────────────────────────────

@astro.get("/config/debug")
def debug_config(_: None = Depends(validate_api_key)):
    return {
        "bind_chroma": config.chroma_bind,
        "embedding_mode": config.embedding_mode,
        "env": config.deploy_env,
        "project": config.project_id,
    }


@astro.get("/health")
def healthcheck(_: None = Depends(validate_api_key)):
    return {"status": "alive"}


@astro.post("/embed")
def embed(req: EmbedRequest, _: None = Depends(validate_api_key)):
    vector = embed_text(req.text)
    return {"embedding": vector}


@astro.post("/query")
async def query(req: QueryRequest, _: None = Depends(validate_api_key)):
    vector = embed_text(req.query)
    results = await query_collection(chroma_client, req.collection, vector, req.top_k)
    return results


@astro.post("/add")
async def add(req: AddRequest, _: None = Depends(validate_api_key)):
    try:
        result = await add_to_collection(chroma_client, req.collection, req.items)
        return {"status": "ok", "count": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@astro.post("/collection")
async def create_collection_endpoint(req: CreateCollectionRequest, _: None = Depends(validate_api_key)):
    try:
        # スキーマ存在チェック
        schema_path = SCHEMA_DIR / req.schema_file
        if not schema_path.exists():
            raise HTTPException(status_code=400, detail="Schema not found.")

        result = await create_collection(chroma_client, req.name, req.schema_file)
        return {"status": "created", "collection_id": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@astro.get("/collection/{collection_name}/documents")
async def get_documents_by_collection(collection_name: str, _: None = Depends(validate_api_key)):
    try:
        documents = await get_collection_documents(chroma_client, collection_name)
        return {"documents": documents}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@astro.get("/collection/{collection_id}/type")
async def get_collection_type_by_id(collection_id: str, _: None = Depends(validate_api_key)):
    try:
        collection_type = await get_collection_type(chroma_client, collection_id)
        return {"collection_type": collection_type}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@astro.get("/schemas", response_model=List[SchemaDefinition], response_model_exclude_unset=True)
def list_schemas(_: None = Depends(validate_api_key)):
    try:
        schemas = []
        for path in SCHEMA_DIR.glob("*.json"):
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)
                schema = SchemaDefinition(**data)
                schemas.append(schema)
        return schemas
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

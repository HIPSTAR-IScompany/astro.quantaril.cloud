from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from typing import Optional, List
from pathlib import Path
from datetime import datetime
import os
import json

from astro.utils import load_config, load_dotenv_config
from astro.chroma_client import (
    get_chroma_client,
    query_collection,
    add_to_collection,
    create_collection,
    get_collection_documents,
    get_collection_type
)
from astro.embedder import embed_text
from astro.models import DocumentItem, SchemaDefinition

# ─── 初期化 ───
load_dotenv_config()
config = load_config()
astro = FastAPI()
chroma_client = get_chroma_client()
SCHEMA_DIR = Path(config.schema_dir)
BEARER_DIR = Path(config.astro_api_key_dir)

# ────────────────────────────────
# APIキー検証ユーティリティ
# ────────────────────────────────
def validate_api_key(authorization: Optional[str] = Header(None)) -> None:
    if config.astro_api_key_mode.lower() != "bearer":
        return
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    token = authorization.replace("Bearer ", "").strip()
    for path in BEARER_DIR.glob("*.json"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if data.get("key") == token:
                deadline = data.get("ExpiryDeadline")
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
def query(req: QueryRequest, _: None = Depends(validate_api_key)):
    vector = embed_text(req.query)
    results = query_collection(chroma_client, req.collection, vector, req.top_k)
    return results


@astro.post("/add")
def add(req: AddRequest, _: None = Depends(validate_api_key)):
    try:
        result = add_to_collection(chroma_client, req.collection, req.items)
        return {"status": "ok", "count": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@astro.post("/collection")
def create_collection_endpoint(req: CreateCollectionRequest, _: None = Depends(validate_api_key)):
    try:
        # スキーマ存在チェック
        schema_path = SCHEMA_DIR / req.schema_file
        if not schema_path.exists():
            raise HTTPException(status_code=400, detail="Schema not found.")

        result = create_collection(chroma_client, req.name, req.schema_file)
        return {"status": "created", "collection_id": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@astro.get("/collection/{collection_name}/documents")
def get_documents_by_collection(collection_name: str, _: None = Depends(validate_api_key)):
    try:
        documents = get_collection_documents(chroma_client, collection_name)
        return {"documents": documents}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@astro.get("/collection/{collection_id}/type")
def get_collection_type_by_id(collection_id: str, _: None = Depends(validate_api_key)):
    try:
        collection_type = get_collection_type(chroma_client, collection_id)
        return {"collection_type": collection_type}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@astro.get("/schemas", response_model=List[SchemaDefinition])
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

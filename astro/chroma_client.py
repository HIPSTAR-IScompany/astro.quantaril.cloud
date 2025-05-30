# app/chroma_client.py

import os
from typing import List, Sequence, Any

import chromadb
from chromadb import AsyncHttpClient
from chromadb.api.async_client import AsyncClientAPI

from astro.models import DocumentItem


# 非同期Chroma HTTPクライアント取得
async def get_chroma_client() -> AsyncClientAPI:
    """非同期モードのChroma HTTPクライアントを取得する。"""
    return await AsyncHttpClient(
        host=os.getenv("CHROMA_HOST", "localhost"),
        port=int(os.getenv("CHROMA_PORT", 8000)),
    )


async def query_collection(
    client: AsyncClientAPI,
    collection: str,
    embedding: Sequence[float],
    top_k: int = 3,
) -> Any:
    """指定コレクションを検索する。"""
    coll = await client.get_collection(name=collection)
    return await coll.query(query_embeddings=[embedding], n_results=top_k)


async def add_to_collection(
    client: AsyncClientAPI,
    collection: str,
    items: List[DocumentItem],
) -> int:
    """ドキュメントをコレクションへ追加する。"""
    coll = await client.get_collection(name=collection)
    ids = [item.id for item in items]
    documents = [item.text for item in items]
    metadatas = [item.metadata or {} for item in items]
    await coll.add(ids=ids, documents=documents, metadatas=metadatas)
    return len(items)


async def create_collection(
    client: AsyncClientAPI,
    name: str,
    schema_file: str,
) -> str:
    """スキーマを指定してコレクションを作成する。"""
    coll = await client.create_collection(name=name, metadata={"schema_file": schema_file})
    return coll.id


async def get_collection_documents(
    client: AsyncClientAPI,
    collection: str,
) -> List[str]:
    """コレクション内の全ドキュメントを取得する。"""
    coll = await client.get_collection(name=collection)
    result = await coll.get()
    return result.get("documents", [])


async def get_collection_type(
    client: AsyncClientAPI,
    collection: str,
) -> Any:
    """コレクションに設定されたスキーマ名を取得する。"""
    coll = await client.get_collection(name=collection)
    return coll.metadata.get("schema_file")

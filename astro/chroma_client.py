# app/chroma_client.py

import os
import chromadb
from chromadb.api.async_client import AsyncHttpClient

# 非同期Chroma HTTPクライアント取得
async def get_chroma_client() -> AsyncHttpClient:
    """
    非同期モードのChroma HTTPクライアントを取得する。
    Chroma Server は別プロセスで起動しておく必要がある。
    """
    return await chromadb.AsyncHttpClient(
        host=os.getenv("CHROMA_HOST", "localhost"),
        port=int(os.getenv("CHROMA_PORT", 8000))
    )
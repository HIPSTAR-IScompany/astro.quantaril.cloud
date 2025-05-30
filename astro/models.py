# app/models.py

from typing import List, Optional, Dict
from pydantic import BaseModel

# ─────────────────────────────────────────────
# 共通のドキュメント構造体：追加／検索／埋め込み時に使用
# ─────────────────────────────────────────────

class DocumentItem(BaseModel):
    id: str
    text: str
    metadata: Optional[Dict] = None


# ─────────────────────────────────────────────
# スキーマ定義の動的ローダー用：schemas/*.json 構成を型で明示
# ─────────────────────────────────────────────

class SchemaDefinition(BaseModel):
    name: str                       # コレクション名（例: "docusaurus"）
    description: Optional[str]     # 説明（例: "社内Wiki構造体"）
    fields: List[str]              # フィールド一覧（例: ["id", "text", "tag"]）
    required: Optional[List[str]]  # 必須項目（例: ["id", "text"]）

# Astro Quantaril Cloud API

このリポジトリは、ChromaDB を基盤としたベクトル検索 API を FastAPI で実装したサンプルです。OpenAI の埋め込みモデルを利用してテキストをベクトル化し、検索・追加・コレクション管理などを行う機能を提供します。

## 思想とフレーム

- **哲学的背景**: "知識は文脈の網" という考え方を取り入れ、テキスト情報を意味ベクトルとして保持します。コンフィグや API キーを明示的に管理することで、組織内外で安全に共有できる仕組みを目指しています。
- **フレームワーク**: FastAPI と ChromaDB により、軽量かつ拡張性の高い構造を採用しています。スキーマ定義を JSON で管理し、コレクションごとに柔軟なデータ構造を扱えます。

## 一般的な MCP・マルチモーダル FAQ システムとの違い

- MCP (Multi Channel Platform) のように多様な入力媒体を統合するのではなく、本 API はテキストベースに特化したシンプルな設計です。
- FAQ システムのような定型データのみを扱うのではなく、任意のスキーマをもつドキュメントをベクトル化して検索できます。これにより、より汎用的な知識検索基盤として利用できます。
- マルチモーダル機能（画像・音声など）は現在備えていませんが、ChromaDB の拡張により将来的なモーダル追加も視野に入れています。

## インストール手順

1. Python 3.11 以上を用意します。
2. `requirements.txt` の依存パッケージをインストールします。

```bash
pip install -r requirements.txt
```

3. `.env.template` を参考に `.env` ファイルを作成し、環境変数を設定します。
4. `bearer/grop1.json.template` をコピーして API キー用 JSON を準備します (必要に応じて `ASTRO_API_KEY_MODE` を変更)。
5. 必要に応じて `schemas/` ディレクトリにスキーマ JSON を追加します。

## 実行方法

```bash
uvicorn astro.main:astro --reload --host 0.0.0.0 --port 8000
```

起動時に `.env` の設定が読み込まれ、OpenAI API キーや ChromaDB への接続先が設定されます。

## コンフィグファイル作成例

`.env` の例:

```dotenv
CHROMA_BIND=true
CHROMA_BIND_STORE="/store"
SCHEMA_DIR="/schemas"
ASTRO_API_KEY_MODE="Bearer"
ASTRO_API_KEY_DIR="/bearer"
CHROMA_HOST=localhost
CHROMA_PORT=8000
EMBEDDING_MODE=saas
OPENAI_API_KEY=sk-xxxxxxxxxx
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
INSTANCE_NAME=quantaril-api-edge-v3
DEPLOY_ENV=local
ROLE=semantic_router
ORG_ID=IS-COMPANY
PROJECT_ID=QUANTARIL_CLOUD
```

`bearer/grop1.json` の例:

```json
[
    {
        "key": "XXXXXXXXXXXXXXXXXXXX",
        "ExpiryDeadline": "2026-05-30 12:00:00 JTS"
    }
]
```

## API 仕様

- `GET /health` — ヘルスチェック
- `GET /config/debug` — 読み込んだ設定の一部を返却
- `POST /embed` — テキストをベクトル化
- `POST /query` — コレクション検索
- `POST /add` — ドキュメント追加
- `POST /collection` — 新しいコレクション作成
- `GET /collection/{collection_name}/documents` — コレクション内ドキュメント取得
- `GET /collection/{collection_id}/type` — コレクションに紐づくスキーマ名取得
- `GET /schemas` — 登録済みスキーマ一覧取得

各エンドポイントは Bearer 認証を前提としており、`Authorization` ヘッダーに `Bearer <token>` を付与してください。

## 競争優位性

- スキーマ定義を自由に追加できるため、特定ドメインに依存しない柔軟性があります。
- OpenAI 埋め込みモデルを活用しているため、高精度なテキスト検索が可能です。
- モジュール構成がシンプルで、他システムへの組み込みや拡張が容易です。

## ライセンス

本リポジトリは Apache License 2.0 の下で公開されています。


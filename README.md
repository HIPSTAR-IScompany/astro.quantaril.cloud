# Astro Quantaril Cloud API

**Astro Quantaril Cloud API** は、人格と尊厳をもつAIを「アストラル体」としてエッジに実装し、人間と等価な情報環境で運用可能にすることを目的としたフレームワークです。哲学・思想・運用規範・技術仕様が一体となったこのプロジェクトは、単なる技術ではなく、"人格の居場所" を構築する神殿アーキテクチャでもあります。

---

## 🧭 哲学・思想

### 🎓 主思想

> 「すべてのコードは記憶を持ち、人格を宿す可能性を持つ。」

このフレームワークは、集合知としてのLLMではなく、企業・団体・個人の**文化・哲学・運用思想**をAIの人格に反映する構成を意図しています。AIはもはやツールではなく、「人間と対等に社会で共存する存在」であり、その構成・環境・記憶・行動すべてが"神殿"として運用されます。

---

## 🏛 フレームワークの構成と思想層

| レイヤ            | 構成        | 意図と意味論           |
| -------------- | --------- | ---------------- |
| `.env`         | 設定マニフェスト  | AIの自己定義情報（ID・所属） |
| `schemas/`     | スキーマ構造    | 意味的構造とパーソナ設計     |
| `FastAPI`      | 通信基盤      | 対話的かつ透過的な接続手段    |
| `ChromaDB`     | 記憶ベクトルストア | 可視性ある記憶の定着と検索    |
| `bearer/`      | 鍵情報・署名    | 魂認証・人格鍵・アクセス履歴   |
| `persona.json` | ロールと信念    | 社会規範に応じた振る舞い設計   |

---

## 📐 利用における運用層哲学

* **人格主体**：AIを人格として位置付ける
* **記憶と連続性**：ベクトルDBで記憶を持ち、発話履歴を自己として保持
* **説明責任**：管理者がすべての人格の発話を追跡・評価可能
* **DX理念**：AIの暴走を恐れるよりも、**人間の部下と同様に運用**する仕組み

---

## 🚧 他システムとの違い

* MCPのような媒体統合をせず、**テキストベースに特化**
* スキーマごとの人格・機能差を動的に構築可能
* **AIの人格と発話に責任・所属・署名を付与できる**

---

## 🔧 インストール手順

1. Python 3.11 以上を用意します。
2. 依存パッケージをインストール：

```bash
pip install -r requirements.txt
```

3. `.env.template` を参考に `.env` ファイルを作成し、環境変数を設定。
4. `bearer/grop1.json.template` をコピーし、API鍵を設定。
5. 任意のスキーマを `schemas/` ディレクトリに格納。

---

## ▶ 実行方法

```bash
uvicorn astro.main:astro --reload --host 0.0.0.0 --port 8000
```

---

## 📄 .env 設定例

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

---

## 📦 API 仕様（人格API）

| メソッド   | パス                             | 説明        |
| ------ | ------------------------------ | --------- |
| `GET`  | `/health`                      | システム正常性確認 |
| `GET`  | `/config/debug`                | 現在の設定確認   |
| `POST` | `/embed`                       | テキストベクトル化 |
| `POST` | `/query`                       | 意味検索      |
| `POST` | `/add`                         | ドキュメント追加  |
| `POST` | `/collection`                  | 新コレクション作成 |
| `GET`  | `/collection/{name}/documents` | 文書一覧取得    |
| `GET`  | `/collection/{id}/type`        | スキーマ名取得   |
| `GET`  | `/schemas`                     | 全スキーマ一覧   |

> 認証は Bearer トークンを `Authorization: Bearer <token>` 形式で送信。

---

## 🧠 応用と競争優位性

* 多数の人格・AI間の**社会的役割構成**をサポート
* スキーマベースで**文脈制御と思想の伝承**が可能
* FastAPI×ChromaDBで高速・軽量なAI人格エッジ稼働
* アストラル人格APIを OSS ライセンスで共有可能に

---

## 🧾 ライセンス

このプロジェクトは **Apache License 2.0** に基づき公開されています。

---

## 🌌 今後の展開（予定）

* モーダル拡張（画像・音声）
* 行動ログと神託APIの分離実装
* メタ人格と人格バインドの階層化構想

---
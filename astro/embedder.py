from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from astro.utils import load_config

config = load_config()

# APIバージョンなどオプション設定
embedder_kwargs = {
    "api_key": config.openai_api_key,
    "model_name": config.openai_embedding_model,
}

# 任意指定がある場合に追加
if hasattr(config, "openai_api_base"):
    embedder_kwargs["api_base"] = config.openai_api_base
if hasattr(config, "openai_api_type"):
    embedder_kwargs["api_type"] = config.openai_api_type
if hasattr(config, "openai_api_version"):
    embedder_kwargs["api_version"] = config.openai_api_version

# 埋め込み関数初期化
openai_embedder = OpenAIEmbeddingFunction(**embedder_kwargs)

def embed_text(text: str):
    return openai_embedder([text])[0]

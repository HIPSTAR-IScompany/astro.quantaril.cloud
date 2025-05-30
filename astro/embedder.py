from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from astro.utils import AppConfig


def create_embedder(config: AppConfig):
    """設定から OpenAI 埋め込み関数を初期化する"""

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

    openai_embedder = OpenAIEmbeddingFunction(**embedder_kwargs)

    def embed_text(text: str):
        return openai_embedder([text])[0]

    return embed_text

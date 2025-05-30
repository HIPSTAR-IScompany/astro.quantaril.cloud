from pydantic import BaseSettings, Field
from typing import Literal
from dotenv import load_dotenv
from pathlib import Path
import os

# ─── アプリ設定クラス ───
class AppConfig(BaseSettings):
    chroma_bind: bool = Field(default=True, env="CHROMA_BIND")
    chroma_bind_store: str = Field(default="/store", env="CHROMA_BIND_STORE")

    schema_dir: str = Field(default="schemas", env="SCHEMA_DIR")

    chroma_host: str = Field(default="localhost", env="CHROMA_HOST")
    chroma_port: int = Field(default=8000, env="CHROMA_PORT")
    astro_api_key_mode: Literal["Bearer", "none"] = Field(default="Bearer", env="ASTRO_API_KEY_MODE")
    astro_api_key_dir: str = Field(default="/bearer", env="ASTRO_API_KEY_DIR")
    embedding_mode: Literal["saas", "local"] = Field(default="saas", env="EMBEDDING_MODE")
    openai_api_key: str = Field(env="OPENAI_API_KEY")
    openai_embedding_model: str = Field(default="text-embedding-3-small", env="OPENAI_EMBEDDING_MODEL")

    instance_name: str = Field(env="INSTANCE_NAME")
    deploy_env: Literal["local", "production", "staging", "dev", "docker"] = Field(env="DEPLOY_ENV")
    role: str = Field(env="ROLE")

    org_id: str = Field(env="ORG_ID")
    project_id: str = Field(env="PROJECT_ID")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# ─── .envの読み込み ───
def load_dotenv_config(env_path: str = ".env"):
    path = Path(env_path)
    if path.exists():
        load_dotenv(dotenv_path=path)
    else:
        raise FileNotFoundError(f".env file not found at {env_path}")


# ─── 設定読み込み ───
def load_config(env_path: str = ".env") -> AppConfig:
    load_dotenv_config(env_path)
    return AppConfig()


# ─── プロジェクトルートベースでパスを解決 ───
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # astro/ 以下なら2階層上がる
def resolve_schema_path(relative_path: str) -> Path:
    return PROJECT_ROOT / relative_path

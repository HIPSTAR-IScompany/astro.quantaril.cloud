from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Literal
from pathlib import Path
from dotenv import load_dotenv

# ─── アプリ設定クラス ───
class AppConfig(BaseSettings):
    chroma_bind: bool = Field(default=True)
    chroma_bind_store: str = Field(default="store")


    schema_dir: str = Field(default="schemas")

    chroma_host: str = Field(default="localhost")
    chroma_port: int = Field(default=8000)
    astro_api_key_mode: Literal["Bearer", "none"] = Field(default="Bearer")
    astro_api_key_dir: str = Field(default="/bearer")
    embedding_mode: Literal["saas", "local"] = Field(default="saas")
    openai_api_key: str
    openai_embedding_model: str = Field(default="text-embedding-3-small")

    instance_name: str
    deploy_env: Literal["local", "production", "staging", "dev", "docker"]
    role: str

    org_id: str
    project_id: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

def load_dotenv_config(env_file: str = ".env") -> None:
    """Load environment variables from a dotenv file."""
    load_dotenv(env_file)


# ─── 設定読み込み ───
def load_config(env_path: str = ".env") -> AppConfig:
    # env_pathを指定したいときは動的生成
    return AppConfig(_env_file=env_path)


# ─── プロジェクトルートベースでパスを解決 ───
PROJECT_ROOT = Path(__file__).resolve().parents[1]
def resolve_schema_path(relative_path: str) -> Path:
    return PROJECT_ROOT / relative_path


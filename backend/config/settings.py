"""
BungusAI Configuration Settings
Centralized configuration management for the entire application
"""

from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Application
    APP_NAME: str = "BungusAI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # API Configuration
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_PREFIX: str = "/api/v1"
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]

    # Claude/Anthropic API
    CLAUDE_API_KEY: str = os.getenv("CLAUDE_API_KEY", "")
    CLAUDE_MODEL: str = "claude-3-sonnet-20240229"
    CLAUDE_MAX_TOKENS: int = 4096
    CLAUDE_TEMPERATURE: float = 0.7

    # Database Configuration
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost/bungusai"
    )
    DATABASE_ECHO: bool = DEBUG

    # Redis Configuration
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    CACHE_TTL: int = 3600

    # Vector Database (Pinecone)
    PINECONE_API_KEY: Optional[str] = os.getenv("PINECONE_API_KEY", None)
    PINECONE_INDEX_NAME: str = "bungusai-embeddings"
    PINECONE_ENVIRONMENT: str = "us-west1-gcp"

    # OpenAI Configuration (Optional, for vision)
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY", None)

    # JWT Configuration
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Logging
    LOG_LEVEL: str = "INFO" if not DEBUG else "DEBUG"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Model Configurations
    MAX_CONVERSATION_HISTORY: int = 50
    EMBEDDING_DIMENSION: int = 1536

    # Vision Settings
    MAX_IMAGE_SIZE_MB: int = 10
    SUPPORTED_IMAGE_FORMATS: list = ["jpg", "jpeg", "png", "gif", "webp"]

    # NLP Settings
    NLP_LANGUAGE: str = "en"
    SENTIMENT_MODEL: str = "distilbert-base-uncased-finetuned-sst-2-english"

    # Gaming Settings
    GAME_TIMEOUT_SECONDS: int = 300
    MAX_GAME_SESSIONS: int = 1000

    class Config:
        case_sensitive = True
        env_file = ".env"


# Create singleton instance
settings = Settings()

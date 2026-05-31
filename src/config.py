"""Application configuration management."""

import os
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # Telegram Configuration
    telegram_bot_token: str
    telegram_webhook_url: str = "https://localhost/webhook"
    telegram_webhook_port: int = 8443

    # Brawl Stars API
    brawl_stars_api_token: str = ""
    brawl_stars_api_base_url: str = "https://api.brawlstars.com/v1"

    # CoreStats API
    core_stats_api_base_url: str = "https://api.core-stats.com"
    core_stats_api_key: str = ""

    # Database
    database_url: str = "postgresql://user:password@localhost:5432/brawl_stars_draft"
    database_echo: bool = False
    database_pool_size: int = 10
    database_max_overflow: int = 20

    # Application
    app_env: str = "development"
    app_debug: bool = False
    app_log_level: str = "INFO"
    app_port: int = 8000
    app_host: str = "0.0.0.0"

    # Recommendation Engine
    recommendation_weights_config: str = "config/recommendation_weights.json"
    prediction_model_path: str = "models/prediction_model.pkl"
    confidence_threshold: float = 0.6

    # Scheduling
    schedule_update_interval_hours: int = 6
    schedule_prediction_retrain_interval_hours: int = 24
    schedule_meta_snapshot_interval_hours: int = 12

    # Caching
    redis_url: str = "redis://localhost:6379/0"
    cache_ttl_seconds: int = 3600
    cache_enabled: bool = True

    # Feature Flags
    feature_draft_export: bool = True
    feature_team_history: bool = True
    feature_statistics: bool = True
    feature_matchup_viewer: bool = True

    class Config:
        """Pydantic config."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()

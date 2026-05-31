"""Database initialization script."""

import asyncio
import logging

from src.config import settings
from src.database.manager import DatabaseManager
from src.utils.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


async def init_db() -> None:
    """Initialize database schema."""
    logger.info("Initializing database...")
    
    db_manager = DatabaseManager(
        settings.database_url,
        echo=settings.database_echo,
    )
    
    await db_manager.init()
    await db_manager.close()
    
    logger.info("Database initialization complete")


if __name__ == "__main__":
    asyncio.run(init_db())

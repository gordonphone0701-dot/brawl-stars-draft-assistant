"""Application entry point."""

import asyncio
import logging
import sys

from src.bot.main import BotApplication
from src.config import settings
from src.database.manager import DatabaseManager
from src.utils.logging_config import setup_logging


async def main() -> None:
    """Initialize and run the application."""
    # Setup logging
    setup_logging(settings.app_log_level)
    logger = logging.getLogger(__name__)

    try:
        logger.info("Initializing Brawl Stars Draft Assistant Bot")
        logger.info(f"Environment: {settings.app_env}")
        logger.info(f"Debug mode: {settings.app_debug}")

        # Initialize database
        logger.info("Initializing database connection")
        db_manager = DatabaseManager(settings.database_url)
        await db_manager.init()

        # Initialize bot
        logger.info("Initializing Telegram bot")
        bot = BotApplication(db_manager, settings)
        await bot.initialize()

        # Run bot
        logger.info("Starting bot")
        await bot.run()

    except KeyboardInterrupt:
        logger.info("Received interrupt signal")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

"""Data collection pipeline."""

import asyncio
import logging
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from src.data.brawl_stars_api import BrawlStarsAPIClient
from src.data.core_stats_api import CoreStatsAPIClient
from src.data.wiki_scraper import WikiScraper
from src.database.models import Brawler, BrawlerStatistic

logger = logging.getLogger(__name__)


class DataCollectionPipeline:
    """Orchestrate data collection from all sources."""

    def __init__(
        self,
        bs_api_token: str,
        core_stats_key: str,
        session: AsyncSession,
    ):
        """Initialize pipeline.

        Args:
            bs_api_token: Brawl Stars API token
            core_stats_key: CoreStats API key
            session: Database session
        """
        self.bs_api = BrawlStarsAPIClient(bs_api_token)
        self.core_stats = CoreStatsAPIClient(core_stats_key)
        self.wiki = WikiScraper()
        self.session = session

    async def init(self) -> None:
        """Initialize all data sources."""
        logger.info("Initializing data collection pipeline")
        await self.bs_api.init()
        await self.core_stats.init()
        await self.wiki.init()

    async def close(self) -> None:
        """Close all data sources."""
        logger.info("Closing data collection pipeline")
        await self.bs_api.close()
        await self.core_stats.close()
        await self.wiki.close()

    async def collect_brawlers(self) -> None:
        """Collect and update brawler database."""
        logger.info("Collecting brawler data")
        
        # Get brawlers from API
        brawlers = await self.bs_api.get_brawlers()
        if not brawlers:
            logger.warning("Failed to fetch brawlers from API")
            return

        for brawler_data in brawlers:
            # Get additional info from wiki
            wiki_info = await self.wiki.get_brawler_info(brawler_data.get("name", ""))
            
            # Upsert brawler
            brawler = await self.session.execute(
                "SELECT * FROM brawler WHERE name = :name",
                {"name": brawler_data.get("name")},
            )
            
            if not brawler:
                brawler = Brawler(
                    name=brawler_data.get("name"),
                    class_name=wiki_info.get("class") if wiki_info else "Unknown",
                    rarity=wiki_info.get("rarity") if wiki_info else None,
                    description=wiki_info.get("description") if wiki_info else None,
                    image_url=wiki_info.get("image_url") if wiki_info else None,
                )
                self.session.add(brawler)
        
        await self.session.commit()
        logger.info(f"Updated {len(brawlers)} brawlers")

    async def collect_statistics(self) -> None:
        """Collect and update statistics."""
        logger.info("Collecting statistics")
        
        # Get meta from CoreStats
        meta = await self.core_stats.get_meta()
        if not meta:
            logger.warning("Failed to fetch meta data")
            return

        # Process and store statistics
        # This is simplified - full implementation would parse meta data
        logger.info("Statistics collection complete")

    async def collect_matchups(self) -> None:
        """Collect and update matchup data."""
        logger.info("Collecting matchup data")
        
        # Get matchups from CoreStats
        matchups = await self.core_stats.get_matchup_matrix()
        if not matchups:
            logger.warning("Failed to fetch matchup data")
            return

        logger.info("Matchup collection complete")

    async def run(self) -> None:
        """Run full data collection pipeline."""
        try:
            await self.init()
            await self.collect_brawlers()
            await self.collect_statistics()
            await self.collect_matchups()
        finally:
            await self.close()

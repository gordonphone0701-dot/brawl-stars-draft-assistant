"""
Configuration settings for Brawl Stars Draft Assistant
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

# Database Configuration
DATABASE_PATH = os.getenv('DATABASE_PATH', 'data/brawl_stars.db')

# Draft Engine Weights
SCORING_WEIGHTS = {
    'map_strength': 0.25,
    'matchup_strength': 0.25,
    'meta_strength': 0.15,
    'draft_safety': 0.15,
    'team_synergy': 0.10,
    'future_prediction': 0.05,
    'pro_usage': 0.05,
    'counterability': -0.15,
    'counter_availability': -0.10,
}

# Update Configuration
UPDATE_INTERVAL_HOURS = 1
AUTO_UPDATE_ENABLED = os.getenv('AUTO_UPDATE_ENABLED', 'true').lower() == 'true'

# Brawler Roles
BRAWLER_ROLES = {
    'Shelly': 'Tank',
    'Nita': 'Tank',
    'Colt': 'Sniper',
    'Bull': 'Tank',
    'Brock': 'Sniper',
    'El Primo': 'Tank',
    'Barley': 'Control',
    'Poco': 'Support',
    'Rosa': 'Tank',
    'Rico': 'Sniper',
    'Penny': 'Sniper',
    'Darryl': 'Tank',
    'Pam': 'Support',
    'Frank': 'Tank',
    'Mortis': 'Assassin',
    'Val': 'Assassin',
    'Jacky': 'Tank',
    'Gus': 'Support',
    'Nani': 'Sniper',
    'Sprout': 'Control',
    'Tick': 'Control',
    'Leon': 'Assassin',
    'Crow': 'Assassin',
    'Spike': 'Control',
    'Surge': 'Tank',
    'Colette': 'Assassin',
    'Amber': 'Control',
    'Griff': 'Sniper',
    'Gale': 'Control',
    'Squeak': 'Control',
    'Buzz': 'Tank',
    'Edgar': 'Assassin',
    'Stu': 'Assassin',
    'Bea': 'Sniper',
    'Emz': 'Control',
    'Mr. P': 'Support',
    'Byron': 'Support',
    'Ruffs': 'Support',
    'Belle': 'Control',
    'Gene': 'Support',
    'Janet': 'Sniper',
    'RT': 'Tank',
    'Bonnie': 'Support',
    'Lola': 'Support',
    'Sam': 'Tank',
    'Carl': 'Tank',
}

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = 'logs/bot.log'

# Confidence Thresholds
MIN_CONFIDENCE = 50  # Recommendations below 50% confidence are filtered
HIGH_CONFIDENCE = 85  # Recommendations above 85% are marked as "Strong"

# Maps in rotation (sample)
AVAILABLE_MAPS = [
    'Hard Rock Mine',
    'Canal Grande',
    'Showdown',
    'Gem Grab',
    'Bounty',
    'Siege',
    'Heist',
    'Hot Zone',
    'Brawl Ball',
    'Present Plunder',
]

# Feature Flags
ENABLE_FUTURE_PREDICTION = True
ENABLE_ROLE_BALANCE = True
ENABLE_CONFIDENCE_EXPLANATIONS = True

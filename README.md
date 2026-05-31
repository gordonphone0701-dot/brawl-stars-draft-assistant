# Brawl Stars Draft Assistant Bot

A production-ready Telegram bot providing real-time draft recommendations for Brawl Stars competitive play. The system uses advanced competitive analysis, machine learning predictions, and multi-factor scoring to deliver high-quality draft guidance.

## Features

### Intelligent Draft Analysis
- **Multi-factor recommendation engine** combining map performance, matchups, synergies, meta strength, and more
- **Probabilistic draft prediction** anticipating enemy picks based on ranked history and tournament data
- **Confidence scoring** for every recommendation
- **Detailed reasoning** explaining the score behind each pick

### Competitive Data Integration
- Real-time data from Official Brawl Stars API
- Professional tournament statistics from CoreStats
- Automatic meta analysis and trend detection
- Continuous learning from competitive matches

### Telegram Bot Interface
- Quick-start draft creation
- Real-time pick/ban tracking
- Inline recommendations with one-tap selections
- Team composition analysis
- Export draft history
- Statistics lookup

### Fully Automated System
- Automatic data collection from all sources
- Data normalization and validation
- Scheduled statistics updates
- Model retraining from recent matches
- Zero manual intervention required

## Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL 13+
- Telegram Bot Token
- Brawl Stars API Token (optional but recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/gordonphone0701-dot/brawl-stars-draft-assistant.git
cd brawl-stars-draft-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Set up configuration
cp .env.example .env
# Edit .env with your credentials

# Initialize database
python -m src.database.init_db

# Run the bot
python -m src.bot.main
```

### Configuration

See `.env.example` for detailed configuration options.

## Architecture

```
src/
├── bot/                      # Telegram bot interface
├── data/                      # Data collection layer
├── database/                  # Database models and management
├── analytics/                 # Statistics and analysis
├── recommendations/           # Recommendation engine
├── predictions/               # Prediction models
├── utils/                     # Shared utilities
├── config.py                  # Configuration management
└── main.py                    # Application entry point
```

## Data Sources

1. **Official Brawl Stars API** - Player data, battle logs, leaderboards
2. **CoreStats** - Tournament drafts, professional statistics, meta trends
3. **Brawl Stars Wiki** - Brawler database, classifications, metadata

## Recommendation Algorithm

The recommendation engine evaluates each brawler on 15+ factors:

1. Map Strength
2. Matchup Strength
3. Synergy Strength
4. Draft Safety
5. Counterability
6. Counter Availability
7. Meta Strength
8. Competitive Usage
9. Ban Impact
10. Future Draft Prediction
11. Team Composition
12. Draft Flexibility
13. Historical Success
14. Draft State Similarity
15. Confidence Estimation

Each factor is weighted dynamically based on game state and configuration.

## Deployment

### GitHub Actions

Automatic deployment on push to `main` branch.

### Render

```bash
render deploy
```

### Railway

```bash
railway up
```

### Self-Hosted

See documentation for instructions.

## Development

### Running Tests

```bash
pytest tests/ -v
```

### Running with Debug Logging

```bash
DEBUG=1 python -m src.bot.main
```

## Disclaimer

This bot is an unofficial Brawl Stars tool. It is not affiliated with Supercell or Brawl Stars.

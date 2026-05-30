# Brawl Stars Draft Assistant - Telegram Bot

A professional-grade Brawl Stars drafting assistant that provides real-time pick and ban recommendations for Ranked, Scrims, and Competitive play.

## Features

- 🎯 **Multi-Factor Draft Engine** - Analyzes 9 different factors for optimal recommendations
- 📊 **Real-Time Meta Analysis** - Automatically updates from competitive data
- 🤖 **Telegram Bot Interface** - Easy-to-use inline button controls
- 💾 **Persistent Database** - SQLite for all matchup, synergy, and meta data
- ⚡ **Auto-Update System** - Hourly data refresh via GitHub Actions
- 🎮 **Comprehensive Matchup Data** - Win rates, synergies, counterability, draft safety
- 🗺️ **Map-Specific Performance** - Tailored recommendations per map
- 🔮 **Future Pick Prediction** - AI-powered prediction of enemy picks
- 📈 **Confidence Scoring** - Detailed explanations for every recommendation

## Quick Start

### Prerequisites
- Python 3.9+
- Telegram Bot Token
- GitHub Account (for hosting)

### Local Setup

1. Clone the repository
```bash
git clone https://github.com/gordonphone0701-dot/brawl-stars-draft-assistant.git
cd brawl-stars-draft-assistant
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment
```bash
cp .env.example .env
# Edit .env with your Telegram Bot Token
```

5. Initialize database
```bash
python scripts/init_db.py
```

6. Run the bot locally
```bash
python main.py
```

## Telegram Bot Commands

- `/start` - Initialize draft assistant
- `/map <map_name>` - Set current map
- `/pick <brawler>` - Confirm pick for your team
- `/ban <brawler>` - Confirm ban
- `/recommend` - Get top 3 recommendations
- `/meta` - View current meta rankings
- `/export` - Export draft summary
- `/reset` - Start new draft

## Architecture

```
brawl-stars-draft-assistant/
├── main.py                 # Bot entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── config.py              # Configuration settings
│
├── database/
│   ├── db.py              # SQLite connection
│   ├── models.py          # Data models
│   └── schema.sql         # Database schema
│
├── bot/
│   ├── telegram_bot.py    # Bot handlers
│   ├── commands.py        # Command implementations
│   └── keyboards.py       # Inline button layouts
│
├── draft_engine/
│   ├── engine.py          # Core recommendation logic
│   ├── scoring.py         # Scoring algorithm
│   ├── factors.py         # All 9 scoring factors
│   └── prediction.py      # Future pick prediction
│
├── data/
│   ├── ranked.py          # Ranked match data provider
│   ├── esports.py         # Esports data provider
│   ├── maps.py            # Map rotation provider
│   └── meta.py            # Meta strength data
│
├── automation/
│   ├── updater.py         # Auto-update orchestrator
│   └── schedulers.py      # Scheduled tasks
│
├── scripts/
│   ├── init_db.py         # Database initialization
│   └── populate_sample_data.py  # Sample data loader
│
├── .github/workflows/
│   └── auto_update.yml    # GitHub Actions workflow
│
└── docs/
    ├── SETUP.md           # Detailed setup guide
    ├── ARCHITECTURE.md    # System architecture
    ├── DATA_PROVIDERS.md  # How to connect real data
    └── WEIGHTS.md         # Scoring weights config
```

## Draft Engine - The 9 Factors

1. **Map Strength** (25%) - Brawler performance on current map
2. **Matchup Win Rates** (25%) - Effectiveness against enemy team
3. **Meta Strength** (15%) - Current competitive viability
4. **Draft Safety** (15%) - Reliability as blind pick
5. **Team Synergy** (10%) - Chemistry with existing team
6. **Counterability** (-15%) - How easily countered
7. **Counter Availability** (Variable) - How many counters remain
8. **Future Pick Prediction** (5%) - Expected enemy picks
9. **Role Composition** (Auto-balance) - Team role diversity

## Scoring Algorithm

```
score = (map_strength * 0.25)
      + (matchup_strength * 0.25)
      + (meta_strength * 0.15)
      + (draft_safety * 0.15)
      + (team_synergy * 0.10)
      + (future_prediction * 0.05)
      + (pro_usage * 0.05)
      - (counterability * 0.15)
      - (counter_availability_penalty * 0.10)
      + (role_balance_bonus)
```

## Data Sources

The system is designed to work with real data providers:

| Module | Purpose | Status |
|--------|---------|--------|
| `ranked.py` | Fetch high-ranked player matches | Placeholder |
| `esports.py` | Professional esports data | Placeholder |
| `maps.py` | Current map rotation | Placeholder |
| `meta.py` | Meta strength scoring | Placeholder |

See `docs/DATA_PROVIDERS.md` for integration instructions.

## Automation

The bot automatically updates every hour:

1. Fetches latest competitive data
2. Recalculates all matchup statistics
3. Updates meta scores
4. Refreshes synergy values
5. Recomputes draft safety ratings
6. Saves to database
7. Bot immediately uses new values

Powered by GitHub Actions - no external hosting required!

## Deployment

### Option 1: GitHub Actions (Recommended)
- Bot runs on GitHub servers
- Completely free
- Auto-updates hourly
- See `docs/SETUP.md` for details

### Option 2: Render/Railway
- Free tier available
- $7/month after free tier
- See `docs/SETUP.md` for details

### Option 3: Self-Hosted
- Your own server/VPS
- Complete control
- See `docs/SETUP.md` for details

## Configuration

All configuration is in `config.py`:

```python
# Scoring weights
WEIGHTS = {
    'map_strength': 0.25,
    'matchup_strength': 0.25,
    'meta_strength': 0.15,
    'draft_safety': 0.15,
    'team_synergy': 0.10,
    'future_prediction': 0.05,
    'pro_usage': 0.05,
    'counterability': -0.15,
}

# Update frequency
UPDATE_INTERVAL_HOURS = 1
```

## Example Usage

```
User: /start

Bot: 🎮 Brawl Stars Draft Assistant

Map: Hard Rock Mine

Blue Team:
  Belle
  Gus

Red Team:
  (empty)

Bans:
  Janet
  Gene

[Set Map] [Pick] [Ban] [Recommend]

---

User: [Recommend]

Bot: Top Recommendations:

1️⃣ Carl - 92% confidence
   • 90 on Hard Rock Mine
   • Strong into Belle (67%)
   • Safe blind pick
   • Few counters available

2️⃣ Belle - 88% confidence
   • Strong synergy with Gus (82)
   • 85 on current map

3️⃣ Gus - 84% confidence
   • High meta strength (88)
   • Strong into RT (71%)

[Pick Carl] [Pick Belle] [Pick Gus] [Undo] [Export]
```

## Contributing

This project is designed to be easily maintainable and extensible:

- Modular architecture
- Full documentation
- Clear separation of concerns
- Production-ready error handling
- Comprehensive logging

See `docs/ARCHITECTURE.md` for contribution guidelines.

## License

MIT License - See LICENSE file

## Support

For issues, questions, or suggestions, please open a GitHub issue.

---

**Built with ❤️ for the Brawl Stars competitive community**

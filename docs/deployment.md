"""Deployment guide for various platforms."""

# Deployment Guide

## Table of Contents

1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Render](#render)
4. [Railway](#railway)
5. [Self-Hosted Linux](#self-hosted-linux)
6. [Monitoring](#monitoring)

## Local Development

### Setup

```bash
# Clone and setup
git clone https://github.com/gordonphone0701-dot/brawl-stars-draft-assistant.git
cd brawl-stars-draft-assistant

# Create environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your values

# Initialize database
python -m src.database.init_db

# Run
python -m src.bot.main
```

## Docker Deployment

### Build Image

```bash
docker build -t brawl-stars-bot:latest .
```

### Run Container

```bash
docker run \
  -e DATABASE_URL=postgresql://user:pass@db:5432/brawl_stars \
  -e TELEGRAM_BOT_TOKEN=your_token \
  -e BRAWL_STARS_API_TOKEN=your_token \
  brawl-stars-bot:latest
```

### Docker Compose (Recommended for local)

```bash
docker-compose up -d
docker-compose logs -f bot
```

## Render Deployment

### 1. Connect Repository

- Go to https://render.com
- Click "New +"
- Select "Web Service"
- Connect your GitHub repository

### 2. Configure Service

- **Name:** brawl-stars-bot
- **Environment:** Python 3
- **Region:** Choose closest to you
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python -m src.bot.main`

### 3. Set Environment Variables

In Render dashboard, go to "Environment":

```
DATABASE_URL = postgresql://...
TELEGRAM_BOT_TOKEN = your_token
BRAWL_STARS_API_TOKEN = your_token
CORE_STATS_API_KEY = your_key
APP_ENV = production
SCHEDULE_UPDATE_INTERVAL_HOURS = 6
```

### 4. Add PostgreSQL

- Click "New +"
- Select "PostgreSQL"
- Name it "brawl-stars-db"
- Link it to web service

### 5. Deploy

Click "Deploy" - Render will automatically build and start your bot.

### Monitoring on Render

- View logs: Dashboard > bot > Logs
- Monitor metrics: Dashboard > Metrics
- Set up alerts: Account > Notifications

## Railway Deployment

### 1. Connect Repository

- Go to https://railway.app
- Click "New Project"
- Select "Deploy from GitHub"
- Connect your repository

### 2. Configure Services

Railway auto-detects `railway.json`:

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "dockerfile"
  },
  "deploy": {
    "restartPolicyType": "always"
  },
  "plugins": [
    "https://github.com/railwayapp/plugins/releases/download/v0.1.0/postgres"
  ]
}
```

### 3. Set Environment Variables

In Railway console:

```
TELEGRAM_BOT_TOKEN=your_token
BRAWL_STARS_API_TOKEN=your_token
CORE_STATS_API_KEY=your_key
APP_ENV=production
DATABASE_URL=postgresql://...
```

### 4. Deploy

Push to main branch - Railway will auto-deploy.

### Monitoring on Railway

- View logs: Project > Logs
- Monitor resources: Project > Metrics
- Set alerts: Project > Settings

## Self-Hosted Linux

### Prerequisites

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y \
  python3.10 \
  python3.10-venv \
  postgresql \
  redis-server \
  supervisor \
  nginx
```

### Setup

```bash
# Create user
sudo useradd -m brawl-bot
sudo su - brawl-bot

# Clone repo
git clone https://github.com/gordonphone0701-dot/brawl-stars-draft-assistant.git
cd brawl-stars-draft-assistant

# Setup Python
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with production values

# Initialize database
python -m src.database.init_db
```

### Setup Supervisor

Create `/etc/supervisor/conf.d/brawl-bot.conf`:

```ini
[program:brawl-bot]
directory=/home/brawl-bot/brawl-stars-draft-assistant
command=/home/brawl-bot/brawl-stars-draft-assistant/venv/bin/python -m src.bot.main
user=brawl-bot
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/brawl-bot/brawl-stars-draft-assistant/logs/app.log
environment=PATH="/home/brawl-bot/brawl-stars-draft-assistant/venv/bin"
```

### Start Service

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start brawl-bot
sudo supervisorctl status
```

### Setup Nginx

Create `/etc/nginx/sites-available/brawl-bot`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable and test:

```bash
sudo ln -s /etc/nginx/sites-available/brawl-bot /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Setup SSL

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Monitoring

### Logging

Check logs in real-time:

```bash
# Docker
docker-compose logs -f bot

# Local
tail -f logs/app.log

# Linux service
sudo tail -f /home/brawl-bot/brawl-stars-draft-assistant/logs/app.log
```

### Health Checks

Monitor bot health:

```python
# Check database connection
python -c "from src.database.manager import DatabaseManager; await DatabaseManager(...).init()"

# Check API connectivity
python -c "from src.data.brawl_stars_api import BrawlStarsAPIClient; await BrawlStarsAPIClient(...).init()"
```

### Metrics to Monitor

- Bot message latency
- Database connection pool usage
- API error rates
- CPU and memory usage
- Disk space for logs

### Alerting

Set up alerts for:

- Service crashes
- High error rates
- Database connection failures
- API rate limiting
- Storage warnings

## Scaling Considerations

For high-traffic deployments:

1. **Database:** Enable connection pooling in settings
2. **Caching:** Redis for draft session caching
3. **Load Balancing:** Run multiple bot instances
4. **CDN:** Cache wiki/API responses
5. **Optimization:** Index frequently-queried database columns

## Troubleshooting Deployments

### Bot crashes on startup

```bash
# Check logs
docker-compose logs bot

# Check environment variables
echo $DATABASE_URL
echo $TELEGRAM_BOT_TOKEN

# Verify database
psql $DATABASE_URL -c "SELECT 1"
```

### Database connection refused

```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Test connection
psql -h localhost -U user -d brawl_stars_draft

# Check connection string format
# postgresql://user:password@host:port/database
```

### API errors

```bash
# Check API keys
curl -H "Authorization: Bearer $BRAWL_STARS_API_TOKEN" \
  https://api.brawlstars.com/v1/brawlers

# Check rate limits in response headers
curl -i https://api.brawlstars.com/v1/brawlers
```

## Maintenance

### Regular Tasks

- Monitor logs for errors
- Update dependencies: `pip list --outdated`
- Backup database: `pg_dump $DATABASE_URL > backup.sql`
- Monitor storage usage
- Review performance metrics

### Backups

```bash
# PostgreSQL backup
pg_dump postgresql://user:pass@host/db > backup.sql

# Restore
psql postgresql://user:pass@host/db < backup.sql

# Docker volume backup
docker-compose exec postgres pg_dump -U user brawl_stars_draft > backup.sql
```

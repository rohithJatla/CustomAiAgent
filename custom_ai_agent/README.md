# Custom AI Agent with Google Drive, OCR, and Telegram Bot

## TODO 
## Setup

1. Fill `configs/config.yaml` with  GDrive folder ID and Telegram Bot Token.
2. Install requirements:
```bash
pip install -r requirements.txt
```
3. Run the polling updater:
```bash
python run_polling_updater.py
```
4. Run the Telegram bot server:
```bash
python telegram_bot/bot_server.py
```
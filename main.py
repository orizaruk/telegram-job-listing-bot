import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient

# LOAD API_ID and API_HASH from .env
load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

with TelegramClient(session='sesh', api_id=API_ID, api_hash=API_HASH) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))

import asyncio
import os
import logging
import json
from dotenv import load_dotenv
from telethon import TelegramClient, events

# ENABLE LOGGING
logging.basicConfig(format='[%(levelname) %(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# LOAD API_ID and API_HASH from .env
load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

# CONFIG FOR PERSISTENT STORAGE
CONFIG_FILE = "config.json"

def clear_terminal():
    if os.name == 'nt': # Windows
        os.system('cls') 
    else: # Mac and Linux, should be POSIX
        os.system('clear')
    
def load_config():
    """Load monitored chats and keywords from config.json."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If file doesn't exist, return default empty config and initialize the config file
        return {"chats": [], "keywords": []}
    except json.JSONDecodeError:
        print("Error: config.json is corrupted. Starting with empty config.")
        return {"chats": [], "keywords": []}

# SAVE CONFIG, CONFIG IS A DICT with chats and keywords keys and arrays as values
def save_config(config):
    return

async def manage_chats(client):
    # SAVE THE CLIENT'S DIALOGS INTO AN ARRAY
    dialogs_arr = []
    async for dialog in client.iter_dialogs():
        dialogs_arr.append(dialog.entity)
    print(dialogs_arr)
    # WE WANT TO HAVE 

async def manage_keywords():
    # PRINT THE CURRENT KEYWORDS, PRINT NONE IF LEN() = 0
    # Present add mode and remove mode, and return
    # After add/remove, call save config
    return

async def run_bot(client):
    return
    # Mode 4 - message watcher
    # @client.on(events.NewMessage())
    # async def handler(event):
    #     print(event)
    
    # client.run_until_disconnected()

async def main():

    global config
    global keywords

    config = load_config()    
    keywords = config["keywords"]

    async with TelegramClient(session='sesh', api_id=API_ID, api_hash=API_HASH) as client:
        while True:

            # CHOOSE MODE
            print("\nModes: \n1) Manage Chats \n2) Manage Keywords \n3) Run Monitoring \n4) Exit")
            mode = input("Choose mode (1-4): ")

            clear_terminal()
            
            if mode == '1':
                await manage_chats(client)
            elif mode == '2':
                await manage_keywords()
            elif mode == '3':
                await run_bot(client)
            elif mode == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice, choose 1-4.")
                await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
        

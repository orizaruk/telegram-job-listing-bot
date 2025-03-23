import asyncio
import os
import logging
from dotenv import load_dotenv
from telethon import TelegramClient, events

# ENABLE LOGGING
logging.basicConfig(format='[%(levelname) %(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# LOAD API_ID and API_HASH from .env
load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

"""
TODO: Add logic/modes - the first lists the IDs of the group chat and enables the user to choose which group chats to monitor,
Add keyword manager that allows the user to choose which keywords will be monitored,
A mode to determine where to forward those messages,
and last is the active monitoring enabled mode. 
"""
def clear_terminal():
    if os.name == 'nt': # Windows
        os.system('cls') 
    else: # Mac and Linux, should be POSIX
        os.system('clear')

async def manage_chats(client):
    print("Welcome to the chat manager!")
    await asyncio.sleep(2)
    print("Returning to control flow!")


def manage_keywords():
    print("Welcome to the keyword manager!")

async def run_bot(client):
    return
    # Mode 4 - message watcher
    # @client.on(events.NewMessage())
    # async def handler(event):
    #     print(event)
    
    # client.run_until_disconnected()

async def main():
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
        

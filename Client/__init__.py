from pyrogram import Client
from pytgcalls import PyTgCalls
from Config import SESSION, API_ID, API_HASH



app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)
pytgcalls = PyTgCalls(app)

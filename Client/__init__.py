from pyrogram import Client
from pytgcalls import PyTgCalls
from Config import SESSION, API_ID, API_HASH



app = Client(
    ":memory:",
    API_ID,
    API_HASH,
    SESSION,
    plugins=dict(root="Plugins"),
)
pytgcalls = PyTgCalls(app)



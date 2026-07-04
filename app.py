from flask import Flask
from threading import Thread
import discord
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot is Online ✅", 200

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

TOKEN = os.environ.get('TOKEN')
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} Online')

client.run(TOKEN)

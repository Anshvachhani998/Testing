import asyncio
from pyrogram import Client, filters
import os

API_ID = "21684037"
API_HASH = "cc4dda353688d66c94af69ca48a87bdb"
BOT_TOKEN = "7877654567:AAFLDysG33pCVLnUqfMwgTfLcKDKBfv_taQ"

bot = Client("ansh_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Welcome to the bot.")


    bot.run()

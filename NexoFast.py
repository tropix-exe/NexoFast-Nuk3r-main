import discord
from discord.ext import commands
import asyncio
import os


prefix = "&"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"[+] Logged in as {bot.user.name}#{bot.user.discriminator}")
    print(f"[+] Bot ID: {bot.user.id}")
    print("[+] NexoFast is now online and ready.")


async def load_commands():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"commands.{filename[:-3]}")
                print(f"[+] Loaded: {filename}")
            except Exception as e:
                print(f"[!] Failed to load {filename}: {e}")


async def main():
    async with bot:
        await load_commands()
        await bot.start("")  # If you want to test put your token here

asyncio.run(main())

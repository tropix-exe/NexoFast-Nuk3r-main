import discord
from discord.ext import commands
import asyncio
import os


TOKEN = "MTMyNTU0ODAyNTY0NDMxODg1Mg.G7-Toi.UtZVrdcYZ2OfefuwJj-Z4_2Uutsqyza24moQWI"
PREFIX = "&"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"✅  Logged in as {bot.user} (ID: {bot.user.id})")

async def load_extensions():
    for file in os.listdir("./commands"):
        if file.endswith(".py") and not file.startswith("_"):
            await bot.load_extension(f"commands.{file[:-3]}")
            print(f"🔌  Loaded commands.{file[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())

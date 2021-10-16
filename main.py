import discord
from discord.ext import commands
import os
import youtube_dl

import music

cogs = [music]

client = commands.Bot(command_prefix="!")

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(os.environ["DISCORD_TOKEN"])

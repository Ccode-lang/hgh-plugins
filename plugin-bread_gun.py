import random
from xander_plugin import *

def onload():
    help_menu_edit("!bread", "A command that fires the bread guns at a user. (Reservered for Tweens)")
    log("Bread gun plugin loaded!")

allowed_role = 1221834669373521951
async def onmessage(message):
    if message.content.startswith("!bread ") and checkroles(message.author, message):
        try:
            if config.platform == "discord":
                await message.channel.send(f"{message.mentions[0].mention} was breaded!")
            else:
                await message.channel.send(f"{message.mentions[0].name} was breaded!")
            return False
        except:
            return True
    return True

def checkroles(author, ctx):
    crole = discord.utils.get(ctx.guild.roles, id = allowed_role)
    ret = False
    for role in author.roles:
        if role == crole:
            ret = True
    return ret




def onexit():
    log("Bread gun plugin exit run")

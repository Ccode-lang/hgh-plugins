import uwuify
from xander_plugin import *


def onload():
    help_menu_edit("T-T virus plugin", "A plugin that spreads the T-T virus.")
    log("UwU virus plugin loaded")


async def onmessage(message):
    if ("uwu" in message.content.replace(" ", "").lower()) and (not "uwu virus" in [y.name.lower() for y in message.author.roles]):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="UwU virus"))
        await message.channel.send("The power of the UwU virus has spread and you are now infected!")
    elif ("wuw" in message.content.lower()) and ("uwu virus" in [y.name.lower() for y in message.author.roles]):
        await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="UwU virus"))

    if message.content == "!virus":
        role = discord.utils.get(message.author.guild.roles, name="UwU virus")
        infected = 0
        members = [m for m in message.guild.members]
        for member in members:
            if role in member.roles:
                infected += 1
        await message.channel.send(f"{infected} people are infected in this server.")
        return False
    return True


def onexit():
    log("UwU virus exit run")

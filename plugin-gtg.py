from xander_plugin import *

def onload():
    help_menu_edit("Gtg plugin", "A plugin that reacts to gtg messages.")
    log("Gtg plugin loaded")

async def onmessage(message):
    if message.content.lower() == "gtg school":
        await message.channel.send(f"*The {message.author.mention} has vanished back to the void called school.*")
        return False
    elif message.content.lower() == "gtg thing":
        if config.platform == "discord":
            await message.channel.send(f"*The {message.author.mention} has vanished for unknown reasons.*")
        elif config.platform == "guilded":
            await message.channel.send(f"*The {message.author.name} has vanished for unknown reasons.*")
        return False
    return True

def onexit():
    log("Gtg plugin exit run")
import robospeak as rs

from xander_plugin import *

def onload():
    log("Robot plugin loaded")

async def onmessage(message):
    if message.content.startswith("!robo ") and isinstance(message.channel, discord.DMChannel):
        await message.channel.send(rs.ToRobo(message.content[6:]))
        return False
    

    try:
        await message.channel.send(F"Translation: {rs.FromNums(rs.ToNums(message.content))}")
    except rs.NotDivisibleBy4:
        pass
    except rs.NotRobo:
        pass

    return True

def onexit():
    log("Robot plugin exit run")
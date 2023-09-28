log = None
discord = None
def onload(obj):
    global log
    global discord
    log = obj["log"]
    discord = obj["discord"]
    log("T-T virus plugin loaded")


async def onmessage(message):
    if ("t-t" in message.content.lower()) and (not "t-t virus" in [y.name.lower() for y in message.author.roles]):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="T-T virus"))
        await message.channel.send("The power of the T-T virus has spread and you are now infected!")
    elif ("-t-" in message.content.lower()) and ("t-t virus" in [y.name.lower() for y in message.author.roles]):
        await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="T-T virus"))

    if message.content == "!virus2":
        role = discord.utils.get(message.author.guild.roles, name="T-T virus")
        infected = 0
        members = [m for m in message.guild.members]
        for member in members:
            if role in member.roles:
                infected += 1
        await message.channel.send(f"{infected} people are infected in this server.")
        return False
    return True


def onexit():
    log("T-T virus exit run")

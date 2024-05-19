from xander_plugin import *
from discord.channel import TextChannel
#from discord.threads import Thread


tupperdict = {}


def onload():
    global tupperdict
    help_menu_edit("!addtupp", "A command that adds a tupper through Xander.")
    with open("tuppersave.pydict", "r") as out:
        tupperdict = eval(out.read())
    log("Tupper plugin loaded!")

async def onmessage(message):
    if (message.author.id, message.content.split(" ")[0]) in tupperdict:
        info = tupperdict[(message.author.id, message.content.split(" ")[0])]
        inthread = False
        if type(message.channel) is TextChannel:
            hooks = await message.channel.webhooks()
        else:
            inthread = True
            hooks = await message.channel.parent.webhooks()
        apphook = None
        for hook in hooks:
            if hook.name == "XanderTupp":
                apphook = hook
        if apphook == None:
            if not inthread:
                apphook = await message.channel.create_webhook(name="XanderTupp")
            else:
                apphook = await message.channel.parent.create_webhook(name="XanderTupp")
        if not inthread:
            await apphook.send(message.content[(len(message.content.split(" ")[0]) + 1):], username=info[0] + f" ({message.author.name})", avatar_url=info[1])
        else:
            await apphook.send(message.content[(len(message.content.split(" ")[0]) + 1):], username=info[0] + f" ({message.author.name})", thread=message.channel, avatar_url=info[1])
        await message.delete()
        return False
    elif message.content.startswith("!addtupp "):
        args = message.content[9:].split(" ")
        tupperdict[(message.author.id, args[0])] = (args[1], args[2])
        await message.channel.send("Added tupper")
        return False
    return True

def onexit():
    with open("tuppersave.pydict", "w") as out:
        out.write(str(tupperdict))
    log("Tupper plugin exit run.")
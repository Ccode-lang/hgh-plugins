from xander_plugin import *
from traceback import format_exc

def onload():
    help_menu_edit("!dmsg", "A command that deletes all of a user id's messages.")
    log("Delete messages plugin loaded!")

user = None

def check(ctx):
    global user
    return ctx.author.id == user.id

async def onmessage(message):
    global user
    count = 0
    print(message.guild.channels)
    if message.content.startswith("!dmsg "):
        user = message.guild.get_member(int(message.content[6:]))
        if user:
            for channel in message.guild.channels:
                if not type(channel) is discord.CategoryChannel:
                    while True:
                        deleted = await channel.purge(check=check)
                        for msg in deleted:
                            count += 1
                        log(f"Deleted {count} messages so far")
                        if deleted == []:
                            break
            await message.channel.send("Purged all messages from given user")
            return False
    return True


def onexit():
    log("Delete messages plugin exit run.")
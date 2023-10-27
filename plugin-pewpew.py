import fssdb
import random

from xander_plugin import *

db = None

def onload():
    global db
    help_menu_edit("!shoot", "Shoot a user with a nerf gun.")
    help_menu_edit("!pewscore", "Get your score in pew pew minigame.")
    log("Pew pew plugin loaded!")
    db = fssdb.db(config.fssdbip)

async def onmessage(message):
    global db
    dname = str(message.author.id)
    if message.content.startswith("!shoot "):
        hit = bool(random.getrandbits(1))
        if hit == True:
            await message.channel.send(f"{message.author.mention} shot {message.mentions[0].mention} with a nerf gun!")
            pscore = db.read_point(dname, "pewscore")
            if pscore == "DOESNOTEXIST":
                pscore = "0"
                db.create_dict(dname)
                db.write_point(dname, "pewscore", 0)
            pscore = int(pscore)
            db.write_point(dname, "pewscore", pscore + 1)
        else:
            await message.channel.send(f"{message.mentions[0]} doged {message.author.mention}'s dart!")
        return False
    elif message.content == "!pewscore":
        await message.channel.send(f"Your score is {db.read_point(dname, 'pewscore')}")
    return True


def onexit():
    log("Pew pew plugin exit run.")

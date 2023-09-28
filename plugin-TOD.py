import os
import random


discord = None
log = None

truthlist = []
darelist = []
def onload(obj):
    global discord
    global log
    global truthlist
    global darelist


    discord = obj["discord"]
    log = obj["log"]

    f = open(os.path.join("config", "truth.txt"), "r")
    truthlist = f.readlines()
    f.close()

    f = open(os.path.join("config", "dare.txt"), "r")
    darelist = f.readlines()
    f.close()

    log("Truth or dare plugin loaded.")


async def onmessage(message):
    if message.content == "!truth":
        num = random.randint(0, len(truthlist) - 1)
        truth = truthlist[num]
        await message.channel.send(truth)
        return False
    elif message.content == "!dare":
        num = random.randint(0, len(darelist) - 1)
        dare = darelist[num]
        await message.channel.send(dare)
        return False
    return True

def onexit():
    log("Truth or dare exit called.")
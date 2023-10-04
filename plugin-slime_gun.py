import random
from xander_plugin import *

def onload():
    help_menu_edit("!slime", "A command that fires the slime guns at a user. (Reservered for Momager)")
    log("Slime gun plugin loaded!")

allowed_users = [993653933148995604, 837119081790046228, 886878726686666752, "dlKLOPw4", "AYNqMeG4", "4oxKNYnd"]
gifs = ["https://tenor.com/view/shower-showering-flow-flowing-pouring-gif-12198611", "https://tenor.com/view/lasllen-nickelodeon-kca-kids-choice-awards-chris-pratt-gif-18932606", "https://tenor.com/view/tusareve-katy-perry-slime-nickelodeon-gif-25468694", "https://tenor.com/view/gunge-male-slime-nick-kca-gif-25172114", "https://tenor.com/view/slime-charlie-damelio-splash-kca2021-kids-choice-awards-gif-20736287"]
async def onmessage(message):
    if message.content.startswith("!slime "): # and message.author.id in allowed_users
        gif = gifs[random.randint(0, len(gifs) - 1)]
        try:
            if config.platform == "discord":
                await message.channel.send(f"{message.mentions[0].mention} was slimed!")
            else:
                await message.channel.send(f"{message.mentions[0].name} was slimed!")
            await message.channel.send(gif)
            return False
        except:
            return True
    return True

def onexit():
    log("Slime gun plugin exit run")

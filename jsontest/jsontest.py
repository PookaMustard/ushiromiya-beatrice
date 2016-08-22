import discord
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils.dataIO import fileIO
import json
import os

DATADIR = "data/jsontest"
SETTINGS = DATADIR + "/data.json"

class jsontest:
    """test"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def test(self):
        """Tests this command."""
        login = {}
        with open(SETTINGS, 'r') as f:
            login = json.load(f)
        return self.bot.say(login)


def check_folders():
    if not os.path.exists(DATADIR):
        os.mkdir(DATADIR)
            
def check_files():
    if not fileIO(SETTINGS, "check"):
        emptydict = {'login' : 'blank', 'password' : 'blank'}
        fileIO(SETTINGS, "save", emptydict)

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(jsontest)

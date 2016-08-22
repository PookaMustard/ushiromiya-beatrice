import discord
from discord.ext import commands
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
        return await self.bot.say(login)


def check_folders():
    if not os.path.exists(DATADIR):
        os.mkdir(DATADIR)

def check_files():
    if not dataIO.is_valid_json(SETTINGS):
        emptydict = {'login' : 'blank', 'password' : 'blank'}
        with open (SETTINGS, 'w') as f:
            json.dump(emptydict, f)

def setup(bot):
    check_files()
    check_folders()
    bot.add_cog(jsontest)

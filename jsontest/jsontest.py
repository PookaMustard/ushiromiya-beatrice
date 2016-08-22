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
        login = loadauth()
        return await self.bot.say(login['login'] + login['password'])
        
    @commands.command()
    async def testsave(self, login, password):
        """Tests this command."""
        saveauth(login, password)
        return await self.bot.say('Saved.')


### GLOBAL JSON FUNCTIONS

def saveauth(login, password):
    login = {'login' : login, 'password' : password}
    with open(SETTINGS, 'w') as f:
        json.dump(login, f)
    return

def loadauth():
    login = {}
    with open(SETTINGS, 'r') as f:
        login = json.load(f)
    return login

def check_folders():
    if not os.path.exists(DATADIR):
        os.mkdir(DATADIR)
            
def check_files():
    if not fileIO(SETTINGS, "check"):
        emptydict = {'login' : 'blank', 'password' : 'blank'}
        fileIO(SETTINGS, "save", emptydict)

### BOT SETUP

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(jsontest(bot))

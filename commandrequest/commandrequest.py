import discord
from discord.ext import commands
from cogs.utils import checks
from .utils.dataIO import fileIO
import json
import os

DATADIR = "data/jsontest"
SETTINGS = DATADIR + "/data.json"

class CommandRequest:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def commandrequest(self, ctx, *, command):
        """Sends a request for a new command.
        A modified version of the debug command, with help from Calebj."""
        channelid = loadauth()
        if channelid == '':
            return await self.bot.say("You haven't set the channel ID for command requests correctly.")
        command = command.replace("\'", "\\\'")
        channelid = self.bot.get_channel(str(channelid))
        return await self.bot.send_message(channelid, command)
        
    @commands.command()
    @checks.is_owner()
    async def savechannelid(self, channelid):
        """Saves this channel for commandrequests."""
        saveauth(channelid)
        channelidstring = loadauth()
        return await self.bot.say('Saved.' + channelidstring)
        
### GLOBAL JSON FUNCTIONS

def saveauth(channelid):
    channelid = channelid
    with open(SETTINGS, 'w') as f:
        json.dump(channelid, f)
    return

def loadauth():
    channelid = ''
    with open(SETTINGS, 'r') as f:
        channelid = json.load(f)
    return channelid

def check_folders():
    if not os.path.exists(DATADIR):
        os.mkdir(DATADIR)
            
def check_files():
    if not fileIO(SETTINGS, "check"):
        channelid = ''
        fileIO(SETTINGS, "save", channelid)

### BOT SETUP

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(CommandRequest(bot))


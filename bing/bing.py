from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from __main__ import settings as bot_settings
import requests, requests.utils
import time
import json
import aiohttp
import asyncio
import os
import discord
from discord.ext import commands
from random import randint
from py_bing_search import PyBingImageSearch
from py_bing_search import PyBingWebSearch
from py_bing_search import PyBingVideoSearch
from py_bing_search import PyBingNewsSearch


DIR_DATA = "data/bing"
SETTINGS = DIR_DATA+"/settings.json"
        
class bing:
    """Fetches search results from Bing.
    
    Uses the Python module py_bing_search as a frontend for Red"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO(SETTINGS, "load")
        if self.settings["api_key"] == "":
            print("Cog error: bing, No API key found, please configure me!")
        else:
                self.api_key = self.settings["api_key"]
        self.PREFIXES = bot_settings.prefixes 

    def setadultserver(self, server, status):
        if 'adult' not in self.settings:
               self.settings['adult'] = {}
        if 'servers' not in self.settings['adult']:
               self.settings['adult']['servers'] = {}
#        if 'server' not in self.settings['adult']:
#                self.settings['adult'][server.id] = 'blank'
        self.settings['adult']['servers'][server.id] = status
        fileIO(SETTINGS, "save", self.settings)
        
    def setadultchannel(self, channel, status):
        if 'adult' not in self.settings:
               self.settings['adult'] = {}
        if 'channels' not in self.settings['adult']:
               self.settings['adult']['channels'] = {}
#        if 'server' not in self.settings['adult']:
#                self.settings['adult'][server.id] = 'blank'
        self.settings['adult']['channels'][channel.id] = status
        fileIO(SETTINGS, "save", self.settings)
        
    def getadultserver(self, server):
        if 'adult' not in self.settings or 'servers' not in self.settings['adult'] or if server.id not in self.settings['adult']['servers']:
                return False
        return self.settings['adult']['servers'][server.id]
        
    def getadultchannel(self, channel):
        if 'adult' not in self.settings or 'channels' not in self.settings['adult'] or if channel.id not in self.settings['adult']['channels']:
                return False
        return self.settings['adult']['channels'][channel.id]

    @commands.command()
    async def bing(self, *, text):
        """Fetches an image from Bing, with a moderate SafeSearch setting"""

        retries = 0
        check=''
        if self.settings["api_key"] == "":
                return await self.bot.say("` This cog wasn't configured properly. If you're the owner, add your API key.`")
        if text.split(' ', 1)[0].lower() == 'random':
                text = text.replace('random ', '', 1)
                bing_image = PyBingImageSearch(self.api_key, text, custom_params="&Adult='Strict'")
                result= bing_image.search(limit=99, format='json')
                limit=99
        else:
                bing_image = PyBingImageSearch(self.api_key, text, custom_params="&Adult='Strict'")
                result= bing_image.search(limit=1, format='json')
                limit=0
        while retries <= limit:
                try:
                        check = result[retries].media_url
                        retries = retries + 1
                        limit = retries
                except IndexError:
                        limit = retries
                        break
        if retries == 0:
                bottext = "Cannot find any search results. Try using %bingadult to disable Bing Safe Search."
        else:
                bottext = result[randint(0, limit - 1)].media_url
        await self.bot.say(bottext)
        
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def bingadultsets(self, ctx):
        """Sets %bingadult for entire server"""
            
        server = ctx.message.server
        message = ctx.message
        await self.bot.say("`Do you want to enable %bingadult for this server?` (y/n)")
        response = await self.bot.wait_for_message(author=message.author)
        if response.content.lower().strip() == "y":
                self.setadultserver(server, True)
                await self.bot.say("`Saving server settings now.`")
                strat = self.getadultserver(server)
                await self.bot.say(strat)
        else:
                self.setadultserver(server, False)
                await self.bot.say("`Cancelling server settings now.`")
                strat = self.getadultserver(server)
                await self.bot.say(strat)
                
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def bingadultsetc(self, ctx):
        """Sets %bingadult for entire server"""
            
        server = ctx.message.server
        message = ctx.message
        channel = ctx.message.channel
        await self.bot.say("`Do you want to enable %bingadult for this channel?` (y/n)")
        response = await self.bot.wait_for_message(author=message.author)
        if response.content.lower().strip() == "y":
                self.setadultchannel(channel, True)
                await self.bot.say("`Saving channel settings now.`")
                strat = self.getadultchannel(channel)
                await self.bot.say(strat)
        else:
                self.setadultchannel(channel, False)
                await self.bot.say("`Cancelling channel settings now.`")
                strat = self.getadultchannel(channel)
                await self.bot.say(strat)
        
    @commands.command()
    async def bingsearch(self, *, text):
        """Fetches a search result from Bing"""

        retries = 0
        check=''
        if self.settings["api_key"] == "":
                getKeyUrl = "http://www.myapifilms.com/token.do"
                return await self.bot.say("` This cog wasn't configured properly. If you're the owner, add your API key.`")
        bing_web = PyBingWebSearch(self.api_key, text, web_only=False)
        result= bing_web.search(limit=1, format='json')
        num=0
        try:
                bottext = result[num].url + "\n" + result[num].title + "\n" + result[num].description
        except IndexError:
                bottext = "Cannot find any search results. Try another search."
        await self.bot.say(bottext)
        
    @commands.command()
    async def bingvideo(self, *, text):
        """Fetches a video from Bing"""

        #Your code will go here
        retries = 0
        attempts = 0
        check=''
        if self.settings["api_key"] == "":
                getKeyUrl = "http://www.myapifilms.com/token.do"
                await self.bot.say("` This cog wasn't configured properly. If you're the owner, add your API key.`")
                return
        if text.split(' ', 1)[0].lower() == 'random':
                text = text.replace('random ', '', 1)
                bing_video = PyBingVideoSearch(self.api_key, text)
                result= bing_video.search(limit=99, format='json')
                limit=99
        else:
                bing_video = PyBingVideoSearch(self.api_key, text)
                result= bing_video.search(limit=1, format='json')
                limit=0
        while retries <= limit:
                try:
                        check = result[retries].media_url
                        retries = retries + 1
                        limit = retries
                except IndexError:
                        limit = retries
                        break
        if retries == 0:
                bottext = "Cannot find any search results.."
        else:
                bottext = result[randint(0, limit - 1)].media_url
        while "http://store.steampowered.com/" in bottext or "ign.com" in bottext:
                rng = randint(0, limit - 1)
                bottext = result[rng].media_url
                attempts = attempts + 1
                if attempts <= 20:
                        bottext = "Filtering error. Try this search again."
        await self.bot.say(bottext)
        
    @commands.command()
    async def bingnews(self, *, text):
        """Fetches a news article from Bing"""

        retries = 0
        check=''
        if self.settings["api_key"] == "":
                getKeyUrl = "http://www.myapifilms.com/token.do"
                return await self.bot.say("` This cog wasn't configured properly. If you're the owner, add your API key.`")
        if text.split(' ', 1)[0].lower() == 'random':
                text = text.replace('random ', '', 1)
                bing_news = PyBingNewsSearch(self.api_key, text)
                result= bing_news.search(limit=9, format='json')
                limit=99
        else:
                bing_news = PyBingNewsSearch(self.api_key, text)
                result= bing_news.search(limit=1, format='json')
                limit=0
        while retries <= limit:
                try:
                        check = result[retries].url
                        retries = retries + 1
                        limit = retries
                except IndexError:
                        limit = retries
                        break
        if retries == 0:
                bottext = "Cannot find any search results."
        else:
                num = randint(0, limit - 1)
                time = result[num].date
                time = "Date: " + time
                time = time.replace('T', '\nTime: ')
                time = time.replace('Z', '')
                bottext = result[num].title + "\n" + result[num].url + "\n" + time + "\n" + result[num].description
        await self.bot.say(bottext)
        
    @commands.command(pass_context=True, no_pm=False)
    @checks.admin_or_permissions(manage_server=True)
    async def apikey_bing(self, ctx, key):
        """Set the Bing API key.
        
        Code copied from Mash's IMDB apikey_imdb command"""
        user = ctx.message.author
        if self.settings["api_key"] != "":
            await self.bot.say("{} ` Bing API key found, overwrite it? y/n`".format(user.mention))
            response = await self.bot.wait_for_message(author=ctx.message.author)
            if response.content.lower().strip() == "y":
                self.settings["api_key"] = key
                fileIO(SETTINGS, "save", self.settings)
                await self.bot.say("{} ` Bing API key saved...`".format(user.mention))
            else:
                await self.bot.say("{} `Canceled API key opertation...`".format(user.mention))
        self.settings = fileIO(SETTINGS, "load") 
        self.api_key = self.settings["api_key"]

def check_folders():
    if not os.path.exists(DIR_DATA):
        print("Creating data/bing folder...")
        os.makedirs(DIR_DATA)

def check_files():
    settings = {"api_key": ""}

    if not fileIO(SETTINGS, "check"):
        print("Creating settings.json")
        fileIO(SETTINGS, "save", settings)

def setup(bot):
    check_folders()
    check_files()
    n = bing(bot)
    bot.add_cog(n)

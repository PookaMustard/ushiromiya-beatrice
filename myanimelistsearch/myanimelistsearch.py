import discord
from discord.ext import commands
import spice_api as spice
from bs4 import BeautifulSoup
import aiohttp
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from __main__ import settings as bot_settings
import os
import json

DIR_DATA = "data/myanimelistsearch"
SETTINGS = DIR_DATA+"/settings.json"


class MyAnimeListSearch:
    """Commences a search on MyAnimeList"""

    def __init__(self, bot):
        self.bot = bot
        self.bot = bot
        self.settings = fileIO(SETTINGS, "load")
        if self.settings["username"] == "":
            print("Cog error: MyAnimeListSearch, No MAL login found, please configure me!")
        
    ###
    ### Functions: getsearch, selectsearch
    ###
        
    def getsearch(self, text, medium):
        try:
            try:
                results = spice.search(text, spice.get_medium(medium), self.creds)
            except ValueError:
                checktext = "Search failed. Did you set your login credntials?"
                maxnum = 99
                results = ''
                return checktext, maxnum, results
        except TypeError:
            checktext = "Search failed."
            maxnum = 99
            results = ''
            return checktext, maxnum, results
        retries = 0
        maxnum =0
        checktext=''
        while retries <= 9:
            try:
                context = retries + 1
                checktext = checktext + str(context) + ") " + results[retries].title + "\n"
                retries = retries + 1
                maxnum = maxnum + 1
            except IndexError:
                retries = 10
        return checktext, maxnum, results
        
    def selectsearch(self, response, results, maxnum, medium):
        bottext = ''
        try:
            if maxnum != 1:
                num = int(response.content) - 1
            else:
                num = int(response) - 1
            if (num >= maxnum) or (num < 0):
                bottext = "Chosen number invalid. Assuming first search result.\n\n"
                num=0
        except:
            bottext = "Cannot accept strings for choosing search results. Assuming first search result.\n\n"
            num=0
        if medium == 'anime':
            bottext = bottext + "Title: " + results[num].title + "\n" + "URL: http://myanimelist.net/anime/" + \
                results[num].id + "\n" + "Episodes: " + results[num].episodes + "\n" + "Status: " + \
                results[num].status + "\n" + "MAL Score: " + results[num].score
        elif medium == 'manga':
            bottext = bottext + "Title: " + results[num].title + "\n" + "URL: http://myanimelist.net/manga/" + \
            results[num].id + "\n" + "Volumes: " + results[num].volumes + "\n" + "Chapters: " + \
            results[num].chapters + "\n" + "Status: " + results[num].status + "\n" + "MAL Score: " + \
            results[num].score
        return bottext

    ###
    ### Actual bot commands
    ###

    @commands.command(pass_context=True)
    async def anime(self, ctx, *, text):
        """Returns MAL anime search result using anime name"""

        message = ctx.message
        bottext = ''
        checktext, maxnum, results = self.getsearch(text, 'anime')
        if maxnum == 99:
            return await self.bot.say(checktext)
        elif maxnum != 1:
            await self.bot.say("Found the following anime on MyAnimeList:\n" + checktext + \
            "\nPlease type the number of the anime you want, then send.")
            response = await self.bot.wait_for_message(author=message.author)
        else:
            response = 1
        bottext = self.selectsearch(response, results, maxnum, 'anime')
        return await self.bot.say(bottext)

    @commands.command(pass_context=True)
    async def manga(self, ctx, *, text):
        """Returns MAL manga search result using manga name"""

        message = ctx.message
        bottext = ''
        checktext, maxnum, results = self.getsearch(text, 'manga')
        if maxnum == 99:
            return await self.bot.say(checktext)
        elif maxnum != 1:
            await self.bot.say("Found the following manga on MyAnimeList:\n" + checktext + \
            "\nPlease type the number of the manga you want, then send.")
            response = await self.bot.wait_for_message(author=message.author)
        else:
            response = 1
        bottext = self.selectsearch(response, results, maxnum, 'manga')
        return await self.bot.say(bottext)

    @commands.command()
    async def malcharacter(self, text):
        """Returns MAL character search result using char name"""

        #Your code will go here
        query=text.replace(" ", "%20")
        await self.bot.say("http://myanimelist.net/character.php?q="+query)

    @commands.command()
    async def animelist(self, text):
        """Returns a user's MyAnimeList anime list"""

        #Your code will go here
        query=text
        await self.bot.say("http://myanimelist.net/animelist/"+query)

    @commands.command()
    async def mangalist(self, text):
        """Returns a user's MyAnimeList manga list"""

        #Your code will go here
        query=text
        await self.bot.say("http://myanimelist.net/mangalist/"+query)

    @commands.command()
    async def mal(self, text):
        """Returns MAL search result using search name"""

        #Your code will go here
        query=text.replace(" ", "%20")
        await self.bot.say(" http://myanimelist.net/search/all?q="+query)


    @commands.command(pass_context=True, no_pm=False)
    async def login_mal(self, ctx, username, password):
        """Set the MAL login.
        
        Code copied from Mash's IMDB apikey_imdb command"""
        user = ctx.message.author
        if self.settings["username"] != "":
            await self.bot.say("{} ` MAL Login found, overwrite it? y/n`".format(user.mention))
            response = await self.bot.wait_for_message(author=ctx.message.author)
            if response.content.lower().strip() == "y":
                self.settings["username"] = username
                self.settings["password"] = password
                self.username = self.settings["username"]
                self.password = self.settings["password"]
                self.creds = spice.init_auth(self.username, self.password)
                fileIO(SETTINGS, "save", self.settings)
                await self.bot.say("{} ` MAL Login saved...`".format(user.mention))
            else:
                await self.bot.say("{} `Canceled API key opertation...`".format(user.mention))
        else:
            self.settings["username"] = username
            self.settings["password"] = password
            self.username = self.settings["username"]
            self.password = self.settings["password"]
            self.creds = spice.init_auth(self.username, self.password)
            fileIO(SETTINGS, "save", self.settings)
            await self.bot.say("{} ` MAL Login saved...`".format(user.mention))
        self.settings = fileIO(SETTINGS, "load")

def check_folders():
    if not os.path.exists(DIR_DATA):
        print("Creating data/myanimelistsearch folder...")
        os.makedirs(DIR_DATA)

def check_files():
    settings = {"username": "", "password": ""}

    if not fileIO(SETTINGS, "check"):
        print("Creating settings.json")
        fileIO(SETTINGS, "save", settings)

def setup(bot):
    check_folders()
    check_files()
    n = MyAnimeListSearch(bot)
    bot.add_cog(n)

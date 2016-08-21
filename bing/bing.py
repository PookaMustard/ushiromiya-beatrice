import requests, requests.utils
import time
import json
import discord
from discord.ext import commands
from random import randint
from py_bing_search import PyBingImageSearch
from py_bing_search import PyBingWebSearch
from py_bing_search import PyBingVideoSearch
from py_bing_search import PyBingNewsSearch
        
class bing:
    """Fetches search results from Bing.
    
    Uses the Python module py_bing_search as a frontend for Red"""

    def __init__(self, bot):
        self.bot = bot
        self.api_key = 'WdlwygeDRR0NsUzUZEF4Yql4OLomvvZfp3moFgLl9Zg'

    @commands.command()
    async def bing(self, *, text):
        """Fetches an image from Bing, with a moderate SafeSearch setting"""

        retries = 0
        check=''
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
        
    @commands.command()
    async def bingsearch(self, *, text):
        """Fetches a search result from Bing"""

        retries = 0
        check=''
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

        retries = 0
        check=''
        if text.split(' ', 1)[0].lower() == 'random':
                text = text.replace('random ', '', 1)
                bing_video = PyBingVideoSearch(self.api_key, text)
                result= bing_video.search(limit=99, format='json')
                limit=99
                factlimit=1
        else:
                bing_video = PyBingVideoSearch(self.api_key, text)
                result= bing_video.search(limit=1, format='json')
                limit=0
                factlimit=0
        while retries <= limit:
                try:
                        check = result[retries].media_url
                        retries = retries + 1
                        limit = retries
                except IndexError:
                        limit = retries
                        break
        if retries == 0:
                bottext = "Cannot find any search results."
        else:
                if factlimit == 0:
                        bottext = result[0].media_url
                else:
                        bottext = result[randint(0, limit - 1)].media_url
                # The following code removes any non-video pages, such as Steam and IGN pages which do not even
                # embed any video into Discord.
        while (bottext.find("http://store.steampowered.com/app/") == 1) or \
                      (bottext.find("http://www.ign.com/articles/") == 1):
                        bottext = result[randint(0, limit - 1)].media_url
        await self.bot.say(bottext)
        await self.bot.say('limit = ' + limit + '...retries = ' + retries + '...factlimit = ' + factlimit)
        
    @commands.command()
    async def bingnews(self, *, text):
        """Fetches a news article from Bing"""

        retries = 0
        check=''
        if text.split(' ', 1)[0].lower() == 'random':
                text = text.replace('random ', '', 1)
                bing_news = PyBingNewsSearch(self.api_key, text)
                result= bing_news.search(limit=99, format='json')
                limit=99
        else:
                bing_news = PyBingNewsSearch(self.api_key, text)
                result= bing_news.search(limit=1, format='json')
                num=0
        try:
                bottext = result[num].title + "\n" + result[num].url + "\n" + \
                result[num].date + "\n" + result[num].description
        except IndexError:
                bottext = "Cannot find any search results. Try another search result."
        await self.bot.say(bottext)

def setup(bot):
    bot.add_cog(bing(bot))

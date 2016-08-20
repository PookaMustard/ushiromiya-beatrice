import requests, requests.utils
import time
import json
import discord
from discord.ext import commands
from random import randint
from py_bing_search import PyBingImageSearch
from py_bing_search import PyBingWebSearch
        
class bing:
    """Fetches search results from Bing"""

    def __init__(self, bot):
        self.bot = bot
        api_key = 'WdlwygeDRR0NsUzUZEF4Yql4OLomvvZfp3moFgLl9Zg'

    @commands.command()
    async def bing(self, *, text):
        """Fetches an image from Bing, with a moderate SafeSearch setting"""

        #Your code will go here
        bing_image = PyBingImageSearch(api_key, text, custom_params="&Adult='Strict'")
        if text.split(' ', 1)[0].lower() == 'random':
                result= bing_image.search(limit=100, format='json')
                num=randint(0,99)
        else:
                result= bing_image.search(limit=1, format='json')
                num=0
        try:
                bottext = result[num].media_url
        except IndexError:
                bottext = "Cannot find any search results. Try using %bingadult to disable Bing Safe Search."
        await self.bot.say(bottext)
        
    @commands.command()
    async def bingsearch(self, *, text):
        """Fetches a search result from Bing"""

        #Your code will go here
        bing_web = PyBingWebSearch(api_key, text, web_only=False)
        result= bing_web.search(limit=1, format='json')
        num=0
        try:
                bottext = result[num].url + "\n" + result[num].title + "\n" + result[num].description
        except IndexError:
                bottext = "Cannot find any search results. Try another search."
        await self.bot.say(bottext)

def setup(bot):
    bot.add_cog(bing(bot))

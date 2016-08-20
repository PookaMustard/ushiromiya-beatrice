import requests, requests.utils
import time
import json
import discord
from discord.ext import commands
from py_bing_search import PyBingImageSearch
        
class bing:
    """Fetches search results from Bing"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bing(self, *, text):
        """Fetches an image from Bing, with a moderate SafeSearch setting"""

        #Your code will go here
        bing_image = PyBingImageSearch('WdlwygeDRR0NsUzUZEF4Yql4OLomvvZfp3moFgLl9Zg', '"+text+"', custom_params="&Adult='Strict'")
        result= bing_image.search(limit=1, format='json')
        bottext = result[0].media_url
         await self.bot.say(bottext)

def setup(bot):
    bot.add_cog(bing(bot))

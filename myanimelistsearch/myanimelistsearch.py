import discord
from discord.ext import commands
import spice_api as spice
from bs4 import BeautifulSoup
import aiohttp


class MyAnimeListSearch:
    """Commences a search on MyAnimeList"""

    def __init__(self, bot):
        self.bot = bot
        self.creds = spice.init_auth('Beatrice-BOT', 'Beato-2MR_0')
        
    def getsearch(self, text, medium):
        results = spice.search(text, spice.get_medium(medium), self.creds)
        retries = 0
        maxnum =0
        checktext=''
        while retries <= 9:
            try:
                context = retries + 1
                checktext = checktext + str(context) + ") " + results[retries].title + "\n"
                retries = retries + 1
            except IndexError:
                maxnum = retries
                retries = 10
        return checktext, maxnum

    @commands.command()
    async def anime(self, *text):
        """Returns MAL anime search result using anime name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "%20")
        checktext, maxnum = getsearch(text, 'anime')
        await self.bot.say("Found the following anime on MyAnimeList:\n" + checktext)

    @commands.command()
    async def manga(self, text):
        """Returns MAL manga search result using manga name"""

        #Your code will go here
        query=text.replace(" ", "%20")
        await self.bot.say("http://myanimelist.net/manga.php?q="+query)

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

def setup(bot):
    bot.add_cog(MyAnimeListSearch(bot))

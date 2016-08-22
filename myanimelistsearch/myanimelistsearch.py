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
        try:
            results = spice.search(text, spice.get_medium(medium), self.creds)
        except TypeError:
            checktext = "Search failed."
            maxnum = 99
            return checktext, maxnum
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
        return checktext, maxnum, results
        
    def selectsearch(self, response, results, maxnum, medium):
        try:
            num = int(response.content) - 1
            if (num >= maxnum) or (num < 0):
                bottext = "Chosen number invalid. Assuming first search result.\n\n"
                num=0
            except:
                bottext = "Cannot accept strings for choosing search results. Assuming first search result.\n\n"
                num=0
        if medium == 'anime':
            bottext = bottext + results[num].title +"\n"
        return bottext

    @commands.command(pass_context=True)
    async def anime(self, ctx, *, text):
        """Returns MAL anime search result using anime name"""

        #Your code will go here
        message = ctx.message
        checktext, maxnum, results = self.getsearch(text, 'anime')
        if maxnum == 99:
            return await self.bot.say(checktext)
        elif maxnum != 1:
            await self.bot.say("Found the following anime on MyAnimeList:\n" + checktext + "\nPlease type the number of the game you want, then send.")
            response = await self.bot.wait_for_message(author=message.author)
        else:
            response = 1
        bottext = self.selectsearch(response, results, maxnum, 'anime')
        return await self.bot.say(bottext)

        

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

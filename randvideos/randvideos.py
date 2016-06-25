import discord
from discord.ext import commands

class randvideos:
    """Random videos!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dchipmunk(self):
        """The one and only dramatic chipmunk."""
        await self.bot.say('https://www.youtube.com/watch?v=a1Y73sPHKxw')

    @commands.command()
    async def getready(self):
        """I said get ready."""
        await self.bot.say('https://www.youtube.com/watch?v=ArF8lrby8xY')

    @commands.command()
    async def nostrongfeelings(self):
        """I am neutral."""
        await self.bot.say('https://www.youtube.com/watch?v=CxK_nA2iVXw')

    @commands.command()
    async def nobodycares(self):
        """And nobody ever will."""
        await self.bot.say('https://www.youtube.com/watch?v=Lrr_VVtyUA8')
        
    @commands.command()
    async def aha(self):
        """Starring Alan Partridge."""
        await self.bot.say('https://www.youtube.com/watch?v=uuN7kOW7iwo')

    @commands.command()
    async def godno(self):
        """PLEASE NO!!!"""
        await self.bot.say('https://www.youtube.com/watch?v=umDr0mPuyQc')
        
    @commands.command()
    async def gameover(self):
        """You died thrice to a Motobug? Seriously?"""
        await self.bot.say('https://www.youtube.com/watch?v=l_Uo0VJihCU')
        
    @commands.command()
    async def knock(self):
        """Knuckles is saying hi."""
        await self.bot.say('https://www.youtube.com/watch?v=CHCgn5pGoQY')
        
def setup(bot):
    bot.add_cog(randvideos(bot))

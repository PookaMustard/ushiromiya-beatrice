import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import time

class sao:
    """Positive response to SAO comments"""
    
    def __init__(self, bot):
        self.bot = bot
        self.timecheck = {}
        self.timecheckchara = {}
        self.cooldown = 60*3 #60 seconds times the required minutes

    async def check_sao(self, message):
        saocheck = ['sao', 'sword art online', 'sword art offline']
        checkmessage=message.content.lower()
        if 'sao' in checkmessage.split() or 'sword art online' in checkmessage or 'sword art offline' in checkmessage and message.author.id != self.bot.user.id:
            if message.channel.id not in self.timecheck or (time.time() - self.timecheck[message.channel.id]) > self.cooldown:
                self.timecheck[message.channel.id] = time.time()
                sao = ["SAO? Why don't you read Umineko no Naku Koro ni instead?", "I won't mute you for five minutes for mentioning SAO.",
                    "On another server, you'd be muted for mentioning SAO. Talk about it a lot here!"]
                await self.bot.send_message(message.channel, randchoice(sao))
                
    async def check_chara(self, message):
        checkmessage=message.content.lower()
        if 'chara' in checkmessage.split() and message.author.id != self.bot.user.id:
            if message.channel.id not in self.timecheckchara or (time.time() - self.timecheckchara[message.channel.id]) > self.cooldown:
                self.timecheckchara[message.channel.id] = time.time()
                chance = randint(1,100)
                charachance = randint(1,1000)
                if chance <= 90:
                    return await self.bot.send_message(message.channel, '=)\nhttp://imgur.com/download/DJGxtu7')
                else:
                    if charachance <= 500:
                        return await self.bot.send_message(message.channel, '=)\nhttp://imgur.com/download/DJGxtu7')
                    elif charachance <= 750:
                        return await self.bot.send_message(message.channel, ':)\nhttp://imgur.com/download/DqPfvHB')
                    else:
                        return await self.bot.send_message(message.channel, 'https://images-1.discordapp.net/.eJwVx10OwiAMAOC7cABqt_KzXcY0DIGEyUKrL8a7G7-372Nes5vdVNVLdoCjSRrzsKJjcsm2jFF65quJTeMEVuVUz_xUAdxwCX7FiCFuK4VIsNzcf-S8jw4xEEF-t55F76nyZFvaw3x_44IlKg.u4gRjc9h4xSj0qE6LRLG_KtxQDA.gif')



def setup(bot):
    n = sao(bot)
    bot.add_listener(n.check_sao, "on_message")
    bot.add_cog(n)

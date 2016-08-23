from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from __main__ import settings as bot_settings
import json
import os
import discord
from discord.ext import commands
from random import randint
from py_bing_search import PyBingImageSearch, PyBingWebSearch, PyBingVideoSearch, PyBingNewsSearch

DATADIR = "data/bing"
SETTINGS = DATADIR + "/settings.json"

class NeoBing:
	"""Fetches search results from Bing.
	Uses the Python module py_bing_search as a frontend for Red"""
	
	def __init__(self, bot):
		self.bot = bot
		self.PREFIXES = bot_settings.prefixes 
		
	def getfrombing(self, apikey, text, limit, operation):
		if operation == 'moderateimagesearch':
			bing_obj = PyBingImageSearch(apikey, text, custom_params="&Adult='Moderate'")
		elif operation == 'websearch':
			bing_obj = PyBingWebSearch(apikey, text, , web_only=False)
		result = bing_obj.search(limit=limit, format='json')
		return result
		
	def obtainresult(self, result, operation):
		if operation == 'moderateimagesearch':
			maxnum = len(result)
			return result[randint(1, maxnum) - 1].media_url
		elif operation == 'websearch':
			maxnum = len(result)
			return result[randint(1, maxnum) - 1].url
			
	def limitget(self, text):
		if text.split(' ', 1)[0].lower() == 'random':
			text = text.replace('random ', '', 1)
			limit = 100
		else:
			limit = 1
		return text, limit
		
	def keyerrorcheck(settings):
		
			
	@commands.command(pass_context=True)
	@checks.admin_or_permissions(manage_server=True)
	async def apikey_neobing(self, ctx, key):
		"""Set the Bing API key."""
		settings = loadauth()
		settings['apikey'] = key
		saveauth(settings)
		return await self.bot.say("Bing API key saved.")
		
	@commands.command()
	async def neobing(self, *, text):
		"""Searches Bing for images."""
		settings = loadauth()
		operation = 'moderateimagesearch'
		if settings['apikey'] == '' or settings['apikey'] == 'blank':
			return await self.bot.say("` This cog wasn't configured properly. If you're the owner, add your API key.`")
		apikey = settings['apikey']
		text, limit = self.limitget(text)
		result = self.getfrombing(apikey, text, limit, operation)
		bottext = self.obtainresult(result, operation)
		return await self.bot.say(bottext)
		
	@commands.command()
	async def neobingsearch(self, *, text):
		"""Searches Bing for web results."""
		settings = loadauth()
		operation = 'websearch'
		if settings['apikey'] == '' or settings['apikey'] == 'blank':
			return await self.bot.say("` This cog wasn't configured properly. If you're the owner, add your API key.`")
		apikey = settings['apikey']
		text, limit = self.limitget(text)
		result = self.getfrombing(apikey, text, limit, operation)
		bottext = self.obtainresult(result, operation)
		return await self.bot.say(bottext)

def saveauth(settings):
	settings = settings
	with open(SETTINGS, 'w') as f:
		json.dump(settings, f)
	return

def loadauth():
	settings = {}
	with open(SETTINGS, 'r') as f:
		settings = json.load(f)
	return settings

def check_folders():
	if not os.path.exists(DATADIR):
		print("Creating data directory for Command Request cog")
		os.mkdir(DATADIR)
			
def check_files():
	if not fileIO(SETTINGS, "check"):
		settings = { 'apikey': 'blank', 'adult' : {'servers': {}, 'channels': {}}}
		print("Creating blank data file for Command Request cog")
		fileIO(SETTINGS, "save", settings)

def setup(bot):
	check_folders()
	check_files()
	bot.add_cog(NeoBing(bot))

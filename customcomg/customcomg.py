import discord
from discord.ext import commands
from random import choice as randchoice
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import user_allowed, send_cmd_help
import os
import re

class GlobalCustomCommands:
    """Global custom commands.
       Based off the built-in Custom Commands cog."""

    def __init__(self, bot):
        self.bot = bot
        self.c_commands = fileIO("data/customcomg/commands.json", "load")

    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def gaddcom(self, ctx, command : str, *, text):
        """Adds a global custom command

        Example:
        !addcom yourcommand Text you want
        """
        command = command.lower()
        cmdlist = self.c_commands
        if command in self.bot.commands.keys():
            await self.bot.say("That command is already a standard command.")
            return
        if command not in cmdlist:
            cmdlist[command] = [text]
            self.c_commands = cmdlist
            fileIO("data/customcomg/commands.json", "save", self.c_commands)
            await self.bot.say("Custom command successfully added.")
        else:
            cmdlist[command].append(text)
            fileIO("data/customcomg/commands.json", "save", self.c_commands)
            await self.bot.say("Custom command successfully added.")
            #await self.bot.say("This command already exists. Use editcom to edit it.")

    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def geditcom(self, ctx, command : str):
        """Edits a global custom command

        Example:
        !editcom yourcommand Text you want
        """
        message = ctx.message
        command = command.lower()
        cmdlist = self.c_commands
        if command in cmdlist:
            if len(cmdlist[command])==1:
                await self.bot.say("Enter the new contents of the command.")
                response = await self.bot.wait_for_message(author=message.author)
                cmdlist[command] = [response.content]
                self.c_commands = cmdlist
                fileIO("data/customcomg/commands.json", "save", self.c_commands)
                return await self.bot.say("Custom command successfully edited.")
            else:
                retries = 0
                body = ''
                while retries <= len(cmdlist[command])-1:
                    body = body + str(retries) + ". " + cmdlist[command][retries] + "\n"
                    retries = retries + 1
                await self.bot.say(body + "\nWhich entry do you wish to edit?")
                number = await self.bot.wait_for_message(author=message.author)
                try:
                    if int(number.content) < 0 or int(number.content) > len(cmdlist[command])-1:
                        return await self.bot.say("Chosen number invalid.")
                    number = int(number.content)
                except:
                    return await self.bot.say("Chosen number invalid.")
                await self.bot.say("Enter the new contents of the command.")
                text = await self.bot.wait_for_message(author=message.author)
                cmdlist[command][number] = text.content
                self.c_commands = cmdlist
                fileIO("data/customcomg/commands.json", "save", self.c_commands)
                return await self.bot.say("Custom command successfully edited.")
        else:
            await self.bot.say("That command doesn't exist. Use addcom [command] [text]")

    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def gdelcom(self, ctx, command : str):
        """Deletes a global custom command

        Example:
        !delcom yourcommand"""
        message = ctx.message
        command = command.lower()
        cmdlist = self.c_commands
        if command in cmdlist:
            if len(cmdlist[command])==1:
                cmdlist.pop(command, None)
                self.c_commands = cmdlist
                fileIO("data/customcomg/commands.json", "save", self.c_commands)
                await self.bot.say("Custom command successfully deleted.")
            else:
                retries = 0
                body = ''
                while retries <= len(cmdlist[command])-1:
                    body = body + str(retries) + ". " + cmdlist[command][retries] + "\n"
                    retries = retries + 1
                await self.bot.say(body + "\nWhich entry do you wish to delete? (Type 'all' for all entries)")
                response = await self.bot.wait_for_message(author=message.author)
                try:
                    if response.content.lower() == 'all':
                        cmdlist.pop(command, None)
                        self.c_commands = cmdlist
                        fileIO("data/customcomg/commands.json", "save", self.c_commands)
                        return await self.bot.say("Custom command successfully deleted.")
                    if int(response.content) < 0 or int(response.content) > len(cmdlist[command])-1:
                        return await self.bot.say("Chosen number invalid.")
                    cmdlist[command].pop(int(response.content))
                    fileIO("data/customcomg/commands.json", "save", self.c_commands)
                    await self.bot.say("Custom command successfully deleted.")
                except:
                    return await self.bot.say("Chosen number invalid.")
        else:
            await self.bot.say("That command doesn't exist.")

    @commands.command(pass_context=True, no_pm=True)
    async def gcustomcommands(self, ctx):
        """Shows global custom commands list"""
        cmdlist = self.c_commands
        if cmdlist:
            i = 0
            msg = ["```Custom commands:\n"]
            for cmd in sorted([cmd for cmd in cmdlist.keys()]):
                if len(msg[i]) + len(ctx.prefix) + len(cmd) + 5 > 2000:
                    msg[i] += "```"
                    i += 1
                    msg.append("``` {}{}\n".format(ctx.prefix, cmd))
                else:
                    msg[i] += " {}{}\n".format(ctx.prefix, cmd)
            msg[i] += "```"
            for cmds in msg:
                await self.bot.whisper(cmds)

    async def checkCC(self, message):
        if message.author.id == self.bot.user.id or len(message.content) < 2 or message.channel.is_private:
            return

        if not user_allowed(message):
            return

        msg = message.content
        server = message.server
        prefix = str(self.get_prefix(msg))

        cmdlist = self.c_commands
        cmd = msg[len(prefix):]
        if cmd in cmdlist.keys():
            cmd = randchoice(cmdlist[cmd])
            cmd = self.format_cc(cmd, message)
            await self.bot.send_message(message.channel, cmd)
        elif cmd.lower() in cmdlist.keys():
            cmd = randchoice(cmdlist[cmd.lower()])
            cmd = self.format_cc(cmd, message)
            await self.bot.send_message(message.channel, cmd)

    def get_prefix(self, msg):
        for p in self.bot.command_prefix:
            if msg.startswith(p):
                return p
        return False

    def format_cc(self, command, message):
        results = re.findall("\{([^}]+)\}", command)
        for result in results:
            param = self.transform_parameter(result, message)
            command = command.replace("{" + result + "}", param)
        return command

    def transform_parameter(self, result, message):
        """
        For security reasons only specific objects are allowed
        Internals are ignored
        """
        raw_result = "{" + result + "}"
        objects = {
            "message" : message,
            "author"  : message.author,
            "channel" : message.channel,
            "server"  : message.server
        }
        if result in objects:
            return str(objects[result])
        try:
            first, second = result.split(".")
        except ValueError:
            return raw_result
        if first in objects and not second.startswith("_"):
            first = objects[first]
        else:
            return raw_result
        return str(getattr(first, second, raw_result))


def check_folders():
    if not os.path.exists("data/customcomg"):
        print("Creating data/customcomg folder...")
        os.makedirs("data/customcomg")

def check_files():
    f = "data/customcomg/commands.json"
    if not fileIO(f, "check"):
        print("Creating empty commands.json...")
        fileIO(f, "save", {})

def setup(bot):
    check_folders()
    check_files()
    n = GlobalCustomCommands(bot)
    bot.add_listener(n.checkCC, "on_message")
    bot.add_cog(n)
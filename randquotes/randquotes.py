import discord 
from discord.ext import commands
from random import randint
from random import choice as randchoice
from cogs.utils import checks
from __main__ import set_cog, send_cmd_help, settings

class randquotes: 
    """Random quotes!""" 

    def __init__(self, bot): 
        self.bot = bot 

    @commands.command()
    async def steamrant(self): 
        """Yes. Water.""" 
        await self.bot.say("In order to use Steam, you have to sign yourself into a contract which basically says \"YOU OWN NOTHING.\" The end result is that you end up buying licenses to games, which they can revoke anytime they wanted. They require the internet for the validation of licenses, which shouldn't be a requirement to play single player games. This results in an ecosystem that basically controls the titles you owned and gives you none of it, forcing you to stay into the ecosystem through the client to play the games you bought even if you don't want the client.")
        await self.bot.say("The best part about all of this is that they can change their contract terms and retroactively apply it onto all the games bought under the previous term. If you don't accept the changes, your account is terminated along with the licenses you've bought under the old terms. You only get to keep the licenses you bought under the old terms IF you agree to them retroactively applying the new terms onto them.")
        await self.bot.say("The end.")

    @commands.command()
    async def callforhelp(self): 
        """I hate Flowey.""" 
        await self.bot.say("But nobody came.")

    @commands.command()
    async def badtime(self):
        """Sans Strikes Back.""" 
        badtime = ["You don't really want to click this link!\nhttps://jcw87.github.io/c2-sans-fight/",
                   "You don't really want to click this link!\nhttps://joezeng.github.io/endless-sans/"]
        await self.bot.say(randchoice(badtime))

    @commands.command()
    async def fairdyne(self):
        """The Undying"""
        await self.bot.say("NGAHHH!!\nhttps://joezeng.github.io/fairdyne/")
        
    @commands.command()
    async def am2r(self):
        """Another Metroid Encore Rem- I mean Another Metroid 2 Remake"""
        await self.bot.say("Currently available builds:\n•Windows: 1.0, 1.1\n•Linux: 1.0, 1.1\n•Mac: 1.1\nhttps://1drv.ms/f/s!Ar6sDvz1zhVkqE57a-TKs1HznzAF")
        
    @commands.command()
    async def pokemonuranium(self):
        """It's a titanium fangame!"""
        await self.bot.say("https://1drv.ms/f/s!Ar6sDvz1zhVkqH4Yk5CX69DoDPKN")
        
    @commands.command()
    async def sm2du(self):
        """Oh Nintendo, why do you have to force me to keep doing this!"""
        await self.bot.say("https://www.mediafire.com/?ur6c8cfa42pz1g5")

    @commands.command()
    async def ia(self): 
        """INDIE ASSAULTED""" 
        ia = ["I would like to report this game for Indie Sexual Assault", "Spade was based off Sonic right? Then why is everyone complaining that he has a spindash?",
              "https://youtu.be/5XsLEXSyINs"]
        await self.bot.say(randchoice(ia))
        
    @commands.command()
    async def ign(self): 
        """International Games...Network?""" 
        ign = ["```Too much fun.```\n-IGN",
               "```Clearly all Sonic fans want is to fuck Big the Cat.```\n-IGN",
               "```too much water not enough Donald Trump looking pokemon```\n-IGN",
               "```The definitive example of the genre 2/10```\n-IGN",
               "```It's good except that it's sonic 0/10```\n-IGN",
               "`> Sonic was always bad`\n`> Sonic CD is one of our top 100 games`\n-IGN",
               "```REMOVE ALL WATER```\n-IGN",
               "```splatoon is awesome -no team speak- splatoon sucks```\n-IGN"
               ]
        await self.bot.say(randchoice(ign))

    @commands.command()
    async def fi(self): 
        """And you thought Navi was bad?""" 
        fi = ["YOUR BATTERIES ARE LOW, LINK.", "GOTTA BUY NEW BATTERIES, LINK!",
              "LINK, IT APPEARS YOUR BATTERIES ARE AT 75%. IT WOULD BE A GOOD IDEA TO PAUSE THE GAME AND CHANGE THEM NOW."]
        await self.bot.say(randchoice(fi))

    @commands.command(pass_context=True) 
    async def mn9(self, ctx): 
        """Mighty No. 9: Thoughts"""
        server = ctx.message.server
        if server.id=='174932651201921024':
            return
        else:
            mn9 = ["MIGHTY NO. 9 IS GETTING MIGHTIED OUTTA THE PLANET.", "Mighty No. 9? My pizza is late!!", "Mighty No. 9? How *unmighty*.",
                   "A thousand years would pass and still Mighty No. 9 would be quite the laughing stock...don't you think?", "Even Lambdadelta hates Mighty No. 9.", "4 million dollars did not save this game from turning into a flipping flop.",
                   "https://cdn.discordapp.com/attachments/174932651201921024/194933396621885452/13516359_666046493542630_5062462651910223041_n.png",
                   "https://images-2.discordapp.net/.eJwNx8ERwiAQAMBeKAA4EjnI30-aYJAgiSYeA5fx4di77m8_4my7mMTKXPuk1LL1RG2RnanFkmUhKnuOdesy0aEic0zrkV_cFeDgLWowYIYB0dpRgR_dPxY9OIcODSg-j9veArlE7_t85Q7NWMAnmdAgXLSWj1rE9wcErysP.1U6QQakVUAaZnjyk_Asamb9Bx5Y.jpg?width=287&height=300",
                   "https://67.media.tumblr.com/4fe613d88b23c4f10bc0194409aaf68e/tumblr_nommbxz03Q1qfb2lao1_540.png", "Mighty No. NEIN",
                   "Why buy the game if you can get it for free? Why buy games when you can get them for free, either? https://drive.google.com/folderview?id=0B7NlRHZE9SWSc2hucUlhdmhmMVU&usp=sharing",
                   "If Shovel Knight is the Good, and Azure Gunner Striker is the bad, then Mighty No 9 must be the ugly...", "Hello? Is this Keiji Inafune? Yeah? I'd like to order some pizza.",
                   "Should be called Mighty No. 69'd instead!", "7/10 Not Enough Pizza Explosions -IGN", "I tried to eat some of Mighty No. 9, but I couldn't.",
                   "Asgore didn't hesitate to banish Mighty No. 9 from the Underworld. You must be **THAT BAD** for *Asgore* to do this!", "Seraphna banned this command? Outrageous!", "8.5 Too Much Dashing.",
                   "Mighty No. 9 has been convicted of murdering Megaman in the past. Be careful around it.", "MN9 is the best horror game around...at least according to Steam's 'community'.",
                   "Delivery of pizza has been halted for an unknown reason.", "So yeah, got your money's worth out of the game yet? Oh, wait, this...thing isn't even worth 4 million.",
                   "In the future, someone will burn Scuttle Town again, but with Mighty No. 9 copies.", "Battler tried to play Mighty No. 9...before Jessica smashed the screen...",
                   "Crash Bandicoot wants your love.", "https://cdn.discordapp.com/attachments/173967012123377664/196816534864134155/69087288.jpg", "Spyro is better.",
                   "I once made a pizza out of Mighty No. 9 copies.", "Mighty No. 9 has killed Spongebob. IT IS A HERO!", "Timmy wished that Vicky wouldn't use medieval tools for torturing him. She tortures him with Mighty No. 9 instead.",
                   "Can't wait for Mighty No. 9 creepypasta!", "Where's Mighty No. 8, 7, 6, 5, 4, 3, 2 and 1?! 0/10 bad game.", "Lord Arktivus Brevon was caught with a copy of Mighty No. 9 in his Dreadnought. It must be a horrible game.",
                   "The last time Shantae fought Mighty No. 9, she fainted before the battle even started.", "Mighty No. 9 started the apocalypse. Run.",
                   "Meanwhile at Nintendo Studios...:\nSakura: Why should you be in Smash?\nShantae: Because I think I would be a valuable fighter in your roster\nSakura: Oh ok. What about you?\nBeck: I CAN JUMP AND SHOOT...\nSakura: Oh okayyyyy\nBeck: AND DASH! smiles and winks\nSakura whispers: can someone get him outta here?",
                   "Call's lack of personality makes her the perfect contender for a sex toy", "Mighty No. 9 killed the cat.",
                   "https://images-1.discordapp.net/.eJwFwdsNwyAMAMBdGADHPAxkG0QQSZXUCLtfVXfv3dd81m12c6pO2QGOSxqvw4ryqqPbwTzuXucltvEDVbW28-lvFcDkC6UNHTrvUyIKgIUyUvQhU0AfMEagsuXkcravOczvDxhKIXs.Kkw3TpBf_cvTw3G3CXAsgcI5CX4.jpg",
                   "The Mighty No. 9 Pizza! Is the Pizza! For you and me!", "http://i0.kym-cdn.com/photos/images/newsfeed/001/139/678/2d2.png",
                   "This game is quite dashing..........in a bad way", "Announcing Domino's new special edition pizza: the Mighty Meaty No. 9",
                   "Don't you mean 'Meh'ty Number No. 9?", "When you install a Mighty No. 9 function on your buster\nhttps://cdn.discordapp.com/attachments/173965999744221185/197744572514828289/unknown.png",
                   "I once heard Alex Kidd beat up Beck.", "Damn, that playthrough of MN9 made me hungry for some pizza.",
                   "As much as I give it flak, it's better than FNaF anyday, everyday. *cackles*", "Mighty No. 9 does what Megamandon't.",
                   "Mighty? Yes. Mega? No.", "http://lvl30psy.thecomicseries.com/images/comics/64/e1fc6f772a6cd154c3b027e3a26671f9948643108.png",
                   "I'd rather have Rock and Roll at my Beck and Call", "poor roahmmythril hes gonna have to perfect run this game someday",
                   "Look at my codpiece! You know you want to.\nhttp://media1.gameinformer.com/filestorage/CommunityServer.Components.SiteFiles/imagefeed/featured/comcept/mightyno9/release-date/MightyNo9RD-610.jpg",
                   "http://i.imgur.com/byQgSDr.png","https://cdn.discordapp.com/attachments/173967012123377664/201530405877186560/did-you-mean-0686f1224818a4a6520cd99c626f74ee.png",
                   "I like my Mighty No. 9 with extra anchovies and a garlic cheese stuffed crust.","http://i1.kym-cdn.com/photos/images/newsfeed/001/147/617/a31.png",
                   "http://orig02.deviantart.net/d7cf/f/2016/147/9/f/whatever_by_rongs1234-da3z5ep.png",
                   "```SINCE THE DAWN OF VIDEO GAMES WE HAVE BEEN UNDER A UNIVERSAL UNDERSTANDING THAT 'A' MEANS CONFIRM AND 'B' MEANS CANCEL WHAT THE HELL IS THIS TOM FUCKERY WHO APPROVED THIS```\nhttp://goo.gl/AQqcff",
                   "Not enough pepperoni 9/10 - IGN",
                   "Bubsy, the only game that makes you want to play MN9",
                   "I'd rather spend a millenium playing MN9 than an hour playing Bubsy",
                   "I deleted this game because I'd rather have nothing.",
                   "Expect your delivery time to be 3 years, that'll be 4 million dollars.",
                   "https://scontent.xx.fbcdn.net/v/t1.0-9/14322309_1220766991297729_4294358163529659816_n.jpg?oh=50bf5f6fa73d5631e7305da8ba51199f&oe=587855B9",
                   "Mighty No. $9",
                   "Mighty No. 99 cents",
                   "Beck's got 99 problems and his game is one.",
                   "Here is the coding to the explosions: 3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679",
                   "I got out pizza dough, sauce and cheese, then I put it in the oven, I forgot about that for three years until I opened the oven and out came Mighty No. 9"
                   ]
            return await self.bot.say(randchoice(mn9))

    @commands.command()
    async def sjw(self): 
        """And you thought Navi was bad?""" 
        sjw = ["You're an SJW? So you're a salty juvenile wiener?","SJW: Shameful Jackass Whiner",
               "SJW: Supreme Jackass Whiner","SJW: Super-triggered Justiceless Wanker",
               "SJW: Sexist Jerkass Whiner",
               "https://didyoumean-generator.com/did-you-means/20160714/did-you-mean-66fab343163deb1bac408f4fb30587b4.png",
               "https://cdn.discordapp.com/attachments/207125729299791872/207125770290724865/did-you-mean-dae1b82b3c53652f0c39650bb2a4ce15.png",
               "https://cdn.discordapp.com/attachments/207125729299791872/207125925341560834/did-you-mean-254474a60c4671709b250cafe0a9b9a1.png"]
        await self.bot.say(randchoice(sjw))

    @commands.command()
    async def negotiations(self):
        """The negotiations..."""
        nego = ["NEGOTIATIONS HAS FAILED", "NEGOTIATIONS HAS SUCCEEDED."]
        await self.bot.say(randchoice(nego)) 
        
    @commands.command()
    async def mewquotes(self):
        """^u^"""
        mew = ["```I wrote it all in one shit, while high on caffeine and on boredom.```\n-Mew"]
        await self.bot.say(randchoice(mew))
        
    @commands.command()
    async def mightyneed(self):
        """I don't know what that is."""
        mightyneed = ["http://www.reactiongifs.us/index.html"]
        await self.bot.say(randchoice(mightyneed)) 
        
    @commands.command()
    async def joels(self):
        """..."""
        joels = ["WHOSE BEEN DRAWIN' DICKS?!"]
        await self.bot.say(randchoice(joels)) 
        
    @commands.command()
    async def dicks(self):
        """..."""
        dicks = ["WHOSE BEEN DRAWIN' JOELS?!"]
        await self.bot.say(randchoice(dicks)) 
        
    @commands.command()
    async def tidesofchaos(self):
        """Shameless advertising for fanfiction galore!"""
        sonic = ["```LITERALLY the only good modern SonicxFP story series that makes SonicxSash work```\n-Sonic", 
                "```Literally the only Sonic fanfic that uses the LakeFeperd canon!```\n-ElectricSparx",
                "```The one where Sonic wears pants```\n-RedScarf"]
        await self.bot.say(randchoice(sonic)) 
        
    @commands.command()
    async def badjoke(self):
        """A lot of bad jokes."""
        badjoke = ["```What chatting client let's you go to other worlds? No man's Skype```\n-GigaLem",
                "```What do you call a tuckered out dragon? Crashed Lilac.```\n-GigaLem",
                "```Sash: How do the hell do I dodge bullets?!\nSpade: When the time comes, you won't need to.\nSash: …have you been watching 'The Matrix' again?```\n-RedScarf",
                "```The Good, The Bad, And The Ugly & Knuckles```\n-RedScarf",
                "```What happens when Sam makes her own faction? you get Sam's Club```\n-GigaLem",
                "```why wasn't anyone worried about the junkyard burglary last night?  Because all the thieves did was jack shit```\n-GigaLem",
                "```did you hear about the psychopathic midget that escaped from jail? He's a small medium at large```\n-GigaLem",
                "```What happens if Avalice gets roboticized? Freedom Planet Robobot```\n-GigaLem"
                ]
        await self.bot.say(randchoice(badjoke)) 
        
    @commands.command()
    async def irquotes(self):
        """Presented by Impossible Realms!"""
        irq = ["```HOW ABOUT AN AU WHERE SHANTAE IS A MALE.```\nMens Rights Activists complain about how she is an objectification of men.",
                "```I guess that's the only one then...```\n-Impossible Realms",
                "```...oh, and every time he says \"That's just a Theory, A GAME THEORY\" at the end, it needs to be followed by a 30 minute loop of Mogolovonio.```\n-Impossible Realms"]
        await self.bot.say(randchoice(irq)) 
        
    @commands.command()
    async def ultraquotes(self):
        """From Ultrablockstar!"""
        ultra = ["```I'm not very quotable...```\n-Ultrablockstar",
                 "```I don't fucking care that the Wii and WiiU versions are inverted! Eldin is in the fucking East not the West!```\n-Ultrablockstar",
                 "```Nintendo hates left-handed people now.```\n-Ultrablockstar",
                 "```Am I the only one who scrolls up and read dates?```\n-Ultrablockstar",
                 "```Steam Workshop is a limited piece of crap and sucks all the creativity out of people.```\n-Ultrablockstar",
                 "```Negotiations has failed.```\n-Ultrablockstar",
                 "```Ubisoft is the second worst company in this industry```\n-Ultrablockstar",
                 "```Jagex are the worst thing to ever happen to the gaming industry (with only one good game)```\n-Ultrablockstar",
                 "```I'm not good with button mashing, but I can shake an analog stick mighty fast... I'm just about five years out of practice.```\n-Ultrablockstar",
                 "```The ZXC+Arrow Keys keyboard layout is underrated.```\n-Ultrablockstar",
                 "```The Anti-DRM God has spoken!!!```\n-Ultrablockstar",
                 "```I went pretty deep, no one different```\n-Ultrablockstar",
                 "```My wrists are genuinely in pain```\n-Ultrablockstar"
                 ]
        await self.bot.say(randchoice(ultra)) 

    @commands.command()
    async def bootleg(self):
        """Even I don't know what this command does."""
        bootleg = ["Ribbon Sunflower", "Karen Coffee", "Force", "Mary Shepherd"]
        await self.bot.say(randchoice(bootleg)) 

    @commands.command()
    async def sonicquotes(self):
        """From a user named Sonic!"""
        sonicu = ["```i have a shirt on.```\n-Sonic",
                  "```So how many more memes of me are ya gonna spout out about me in one day?```\n-Sonic",
                  "```If it isn't a chilidog I'm not coming.```\n-Sonic",
                  "```Steam is a lot like politics. Both blow hot air all over the place and take people's money.```\n-Sonic",
                  "```You know what I hate? FUCKING SLICERS ALL OVER THE PLACE.```\n-Sonic",
                  "```PINGAS```\n-Sonic",
                  "```How 'bout them LAKERS!```\n-Sonic",
                  "```Alright, who pissed off Sash and do I need to 'calm her down'?```\n-Sonic",
                  "```How to trigger Pooka: Mention anything FNAF.```\n-Sonic",
                  "```There's a Pooka here... damn, forgot my air pump.```\n-Sonic",
                  "```you have no sympathy from me if you whine about that stupid pit in Mystic Cave.```\n-Sonic",
                  "```I'll fuck you harder than Comcast fucking Giga.```\n-Sonic",
                  "```If it isn't Sash Lilac I'm not c*mming.```\n-Sonic",
                  "```look, I can't ass, okay?```\n-Sonic",
                  "```and no, it doesnt have a usb port i can stick my dick into, so dont even make that joke```\n-Sonic",
                  "https://cdn.discordapp.com/attachments/172098189388808193/222172716151603204/3.jpg",
                  "```hmmm.. what about 'Bitchonary'?```\n-Sonic",
                  "https://pbs.twimg.com/media/CsKrva4WcAABH7m.jpg",
                  "```How about glueing your dick to a girl's vagina?```\n-Sonic",
                  "```his 'video making' is the equivelent of fucking the usb drive on your laptop```\n-Sonic"
                  ]
        await self.bot.say(randchoice(sonicu)) 
        
    @commands.command()
    async def pokefanquotes(self):
        """From Pokefan!"""
        pokefan = ["```>7 houndred\nOH GOD, HE'S GOING MAXIMUM DOG, EVERYONE RUN!```\n-Pokefan",
                   "```There will be an HD remake of Sonic 3 & Knuckles where every single graphic is replaced with Knuckles.```\n-Pokefan",
                   "```I am perfectly fine with Team Mystic, as long as everyone agrees that Team Instinct is a bunch of nazis.```\n-Pokefan",
                   "```It's like calling Ness \"Babe Ruth\" or Papyrus \"Chef Boyardee\"```\n-Pokefan",
                   "```YOU HAD ONE JOB, AND THAT WAS TO GET AN IMAGE OF BINDING OF AVALICE BILL GATES YOU CHEAP PRICK```\n-Pokefan",
                   "```Otherwise we wouldn't have dat A E S T H E T I C B A C K G R O U N D```\n-Pokefan",
                   "```You know the official name is Photoshop Seraphna, right?```\n-Pokefan",
                   "```Geez guys, stop being such bricks to each other!```\n-Pokefan",
                   "```It is fashionable to copulate with flying insects under the scientific classification of Anthophila```\n-Pokefan",
                   ]
        await self.bot.say(randchoice(pokefan)) 
        
    @commands.command()
    async def plomquotes(self):
        """Yes, the creator of that multiva has quotes too."""
        plom = ["```does the break the rules?```\n-Plom510",
                "```Screen my show```\n-Plom510",
                "```What is the sum of 14 and 21?' I'm sorry, my brain isn't working to its fullest right now.```\n-Plom510",
                "```Bingo dies of young age.```\n-Plom510",
                "```What if I take this cow to a strip club?```\n-Plom510",
                "```I never knew she was a guy``` ~Alex Rivero, talking about the first time he met his girlfriend Sam.",
                "```No thanks```\n-Plom510 in response to Fuck 'X'",
                "```five nights at crazy grandma stalking me at night```\n-Plom510",
                "```So I changed my mother's refresh rate to 75 Hertz```\n-Plom510",
                "```I'm gonna stereo quick!```\n-Plom510",
                "```see you in my next game```\n-Plom510"
                ]
        await self.bot.say(randchoice(plom)) 
        
    @commands.command()
    async def epa(self):
        """Planet Wispy."""
        epa = ["```Next stop, Planet Wisp. This attraction is currently off-limits as it is still under construction and may not be dangerous enough for visitors yet.```",
               "```Just a reminder: Please refrain from pushing buttons on the starship. Occasionally, one might jettison you into space. If this happens, your next of kin will be billed for the replacement hatch.```",
               "```Attention! The muscle atrophy simulations will not be open today. We apologize for the inconvenience, but we were not able to find the strength to open it.```",
               "```Would the owner of a white hovercar shaped like an egg please report to the front﻿ desk. Your car has been broken into. Repeat. Would the owner of a white hovercar shaped like an egg please report to the front desk. Your car has been broken in... Wait a minute, WHAT THE HECK?```",
               "```We know they look delicious, but please refrain from licking the rides. That would be disgusting. Do you know where those rides have been? People have been sitting on those rides. With their BUTTS! Okay, go ahead. Lick them. Don’t say we didn’t warn you.```",
               "```Attention ladies and gentlemen! Please make your way over to the main viewing area, where the Light Speed Electrical Parade is about to begi... Ohoh, and, and that concludes the Light Speed Electrical Parade.```",
               "```Please avoid breaking the glass, as it is the only thing between you and ten million gallons of freezing wet death.```",
               "```Every visitor to the park gets a free blue hedgehog! If you catch one, please feel free to take it home with you. Or destroy it. Our choice.```",
               "Please beware of the spikes on the asteroid coaster, they are sharp. Really?﻿ We have to warn people about spikes? Like they won't notice the spikes, I mean, come on! The cars are nothing but spikes! Unbelievable! What... Wa... My... My what is still on?```"
              ]
        await self.bot.say(randchoice(epa)) 
        
    @commands.command()
    async def jontron(self):
        """Just another guy on youtube."""
        #His videos seem to be quotes
        jtron = ["https://www.youtube.com/watch?v=l5xTReubUro",
                "https://www.youtube.com/watch?v=5phl8p3euG4",
                "https://www.youtube.com/watch?v=2aegP8j5al0",
                "https://www.youtube.com/watch?v=qxEwC8vLSD0",
                "https://www.youtube.com/watch?v=uneSOPqqAFw",
                "https://www.youtube.com/watch?v=uWy0JevgS-8",
                "https://www.youtube.com/watch?v=BJEvhi2OlEY",
                "https://www.youtube.com/watch?v=AXzEcwYs8Eo",
                "https://www.youtube.com/watch?v=xrktQmttsfU",
                "https://www.youtube.com/watch?v=-xWoo8y9t_c",
                "https://www.youtube.com/watch?v=7gfxpDx9KZU",
                "https://www.youtube.com/watch?v=0_DCs29xw2A",
                "https://www.youtube.com/watch?v=P7Bl8us5ngk",
                "https://www.youtube.com/watch?v=BpumxLulY7M",
                "https://www.youtube.com/watch?v=r8MjZk_Dw3s",
                "http://24.media.tumblr.com/3f98895ff432cbec39c1052462f64bec/tumblr_n510iaXH771sk0enuo1_500.gif",
                "https://www.youtube.com/watch?v=LFFvJaMhgDg",
                "https://images-1.discordapp.net/.eJwlxlEKgCAMANC7eADXNGp2GzGxoJy49RXdPSLez7vN1Q-zmE21yQKw7pK4r1aUeyzZFuZy5Nh2sYlPiKoxbWeuKoAUMBDiMIxuJCLvwDmaEMnPNAf_1UPln221mOcFK5AjSQ.Ee0aK-SOd-sBYoYFrN4tZnnMLzc"
                ]
        await self.bot.say(randchoice(jtron)) 

    @commands.command()
    async def romanlifeadvice(self):
        """Life advice from Roman!"""
        romanlife = ["```Always ask the bot for support. ```\n-Roman", "```The bot knows best. ```\n-Roman",
                     "```When you're lonely, talk to a bot. ```\n-Roman"]
        await self.bot.say(randchoice(romanlife)) 

    @commands.command()
    async def bingo(self):
        """What is a multiva?"""
        await self.bot.say("WHAT THE FUCK IS A MULTIVA?! ") 
        
    @commands.command()
    async def ridley(self):
        """What? What?! WHAT?!"""
        await self.bot.say("IT'S A-LIVING!") 
        
    @commands.command()
    async def unowen(self):
        """Spoilers to \"And Then There Were None\""""
        await self.bot.say("http://i.imgur.com/ZLNSBaR.jpg\n" +
                           "Flandre has been living in the Scarlet Devil Mansion for at least 495 years, but has never been taken outside and has not seen any humans other than in cooked form. She can destroy anything she wants by crushing it, even destroying a meteor with a single hand and without touching it,which is truly a frightening ability with no real weaknesses.") 
        
    @commands.command()
    async def fp2(self):
        """Sonic Adventure 2"""
        await self.bot.say("https://twitter.com/FPCommunity_txt/status/764934391500079105") 
        
    @commands.command()
    async def cod(self):
        """WARFARE"""
        await self.bot.say("Cowl O' Doody") 
        
    @commands.command()
    async def rohan(self):
        """But it refused?"""
        await self.bot.say("```But, I refuse!```") 
        
    @commands.command()
    async def fixit(self):
        """FIX IT"""
        await self.bot.say("```FIX IT POOKA```")
        
    @commands.command()
    async def bubsy(self):
        """Just like %gowrong"""
        await self.bot.say("```WHAT COULD POSSIBLY GO WRONG?!```")

    @commands.command()
    async def whybing(self):
        """For when someone forces a bing sucks joke"""
        await self.bot.say("```Regardless...whether Bing sucks or not as a search engine, they surely outbeat Google by miles with their development APIs. To demonstrate, I was in a server with a node.js bot. The node.js bot had a Bing and Google image search. The Bing provided full-size images. The Google provided measly thumbnails. That's because the Google command wasn't even using the fullest scope of Google to begin with. Bing on the other hand? They let me extract a ton of data. So instead of having a Google search link, I instead fetch the first (or random) Bing search link and it's finished.```")

    @commands.command()
    async def navyseal(self):
        """You read this already, probably."""
        await self.bot.say("```What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.```")

    @commands.command()
    async def redrant(self):
        """Salt, RedScarf-style"""
        redrants = ["```well, that's what happens when blah blah blah battleaxe blah blah blah broken promises blah blah blah abuse of power blah blah blah```\n-RedScarf",
                    "```that's not brevon, that's a canned extra from A Bug's Life```\n-RedScarf",
                    "```Boom!Sonic: B-\nPlayer: You say 'Bounce Pad' one more time, I'll reach into the screen and tear out all your spines one by one!```\n-RedScarf"]
        await self.bot.say(randchoice(redrants))

    @commands.command()
    async def gametheory(self):
        """The study of mathematical models of conflict and cooperation between intelligent rational decision-makers. Apparently.""" 
        gametheory = ["Game Theory: MatPat is a SHAMELESS MONEYGRABBING CUNT?!?!","Why i gave the pope bayonetta"]
        await self.bot.say(randchoice(gametheory))

    @commands.command()
    async def esquotes(self):
        """Provided to you by ElectricSparx""" 
        chance = randint(1,100)
        es = ["```Your hypocrisy is delicious, your stupidity is spicy, and your ignorance is bland.```\n-ElectricSparx",
              "```Unsurprisingly, your edginess is rather painful.```\n-ElectricSparx",
              "```Ironically, a JonTron voice will not, in fact, work in this situation.```\n-ElectricSparx",
              "```I'm not lazy, just unmotivated.```\n-ElectricSparx",
              "```There is always time for sin.```\n-ElectricSparx",
              "```Error 615: Intelligence Not Found```\n-ElectricSparx",
              "```BRAIN has shut down to avoid damage from stupidity. Please reboot.```\n-ElectricSparx",
              "```ERROR: Brain.dll was unable to be found.```\n-ElectricSparx",
              "```I lack the ability to even give a nanoshit about whatever the fuck you just said.```\n-ElectricSparx",
              "```Higher quality humor than SilvaGunner rips.```\n-ElectricSparx",
              "```FRONTIER COMMUNICATIONS: BRINGING YOU LESS THAN 1 KBPS INTERNET QUALITY SINCE 2016.```\n-ElectricSparx",
              "```I did not come here to watch a bunch of adults act like fucking children.```\n-ElectricSparx",
              "```I LOVE BEING WOKEN UP AT 5 IN THE MORNING TO FIX COMPUTER PROBLEMS!!```\n-ElectricSparx",
              "```Have you heard the good word of our lord and savior, Grand Dad?```\n-ElectricSparx",
              "```It's your favorite thing! H I G H Q U A L I T Y R I P S```\n-ElectricSparx"
              ]
        if chance <= 5:
            return await self.bot.say("```Clearly, thou hast been blessed by the almighty RNGesus.```\n-ElectricSparx")
        else:
            return await self.bot.say(randchoice(es))
            
    @commands.command()
    async def pooka(self):
        """Provided to you by my master!"""
        pooka = ["```\"And I think to myself! What a wonderful world!\"```\n-Not a quote from Pooka, ironically.",
                 "```Never existing is the newest trend in retiring, indeed!```\n-Pooka",
                 "```I am not triggered. I am gainaxed.```\n-Pooka",
                 "***If you complain about us criticizing GT again...may the odds be in your favor.\n-Pooka***",
                 "```Oh. I thought it was a brand of cookies.```\n-Pooka",
                 "```In other words...%chara is the only command with two RNGs until now!!!```\nNo longer true. -Pooka",
                 "```Friendship is not magic. Screw friendship and ponies. MATHEMATICS IS MAGIC.```\n-Pooka",
                 "```You get your games from Steam? Don't you know that steam floats into the sky and then rains later? Just buy your games from Water instead.```\n-Pooka",
                 "```Final Fantasy VIII is undertale- I MEAN UNDERRATED!!```\n-Pooka",
                 "```Valve Steam? WAIT! Steam can come from valves now?! I thought water comes out of valves!!```\n-Pooka",
                 "```So PC Gamer, you're saying that using the C key for crouching makes me a degenerate? Do not worry. I always crouch with the ESC key, and anyone else is doing it wrong. =)```\n-Pooka",
                 "```I can never write 'support the developer' and 'the developer uses DRM' on the same sentence. Wait, did I just write them on the same sentence? What was I talking about?```\n-Pooka",
                 "```How to trigger me: mention anything FNAF.```\nQuote not shamelessly stolen from Sonic. Original quote by Pooka.",
                 "```You have watched the movie to 'finding' a 'fish'. You now suffer from the short term memory loss status ailment. Please contact the nearest White Mage to cure this ailment.```\n-Pooka",
                 "```Seeing your email inbox, which has over a thousand unread mails...it fills you with emailmination.```\n-Pooka",
                 "```I hope my next game will have me invincible to air pumps...```\n-Pooka",
                 "```And this is where I'd have my Wii U...if I had o- sorry, you never heard a variation of this quote before.```\n-Pooka",
                 "```VOTE CHARA FOR PRESIDENT 2016! MAKE THE UNDERGROUND GREAT AGAIN!```\n-Pooka",
                 "```I hope Seraphna isn't reading this quote! For no particular reason at all.```\n-Pooka",
                 "```I never knew that garnets were precious stones! Is that what happens when I take free education?```\n-Pooka",
                 "```From today onwards, if anyone DOES NOT criticize FP2, they will be kicked, and then kicked again, and while kicked, banned. Next will be ultra-banning them. Then final-banning them. Don't ask me how I can kick and ban that much.```\n-Pooka",
                 "```Draw humans. Anthros are overtale- I mean overrated.```\n-Pooka",
                 "```A Metroidvania is a game where Samus fights Dracula in his castle.```\n-Pooka",
                 "```Hi Mr. Cthulhu!!! Nice to meet you!!!```\n-Pooka",
                 "```Why the hell would any game start with a quote from H.P. Lovecraft? Oh wait...you don't tell me...?```\n-Pooka",
                 "```A girl that likes MLP:FiM? WHAT AN ANOMALY!!!!!```\n-Pooka",
                 "```Couldn't they photoshop any better?```\n-Pooka",
                 "```Must resist urge to bake breaks```\n-Pooka",
                 "```%dictoonary irreconciliable ```\n-Pooka",
                 "```Your brickfast is ready```\n-Pooka",
                 "```It was then I realized that you asked for %dick!```\n-Pooka"
                 ]
        await self.bot.say(randchoice(pooka))

    @commands.command()
    async def minha(self):
        """Provided to you by Minha Vida Ordinaria""" 
        minha = ["```Laughter like that of a sea lion having a stroke.```\n-Minha",
        "```I am a lot of quotables```\n-Minha",
        "```Allergic to practically every Liac design.```\n-Minha",
        "```BAKABAKABAKABAKABAKABAKABAKABAKABAKABAKABAKA```\n-Minha",
        "```You're going to die until you get killed!```\n-Minha",
        "```Nananannananaananannaannanananananananananananananananananana's Buried Treasure. Starring Nananananananananananananananannanananananananananananananananananannananana. Nanananananananananananananana. Nanananananannaana.```\n-Minha",
        "```Enjoy! It's join!```\n-Minha",
        "```Oooooooooi, zentê!```\n-Minha",
        "```This is zelicious.```\n-Minha",
        "```The cast of Freedom Planet: Liac, Corol, Butter, Tork, Clover, Gavondorf, Syntagma, Snakeface, Prince Dale, Mayor Jaw, General Panda, Nazeera, and Liac's Dad.```\n-Minha",
        "```Make them bigger.```\n-Minha",
        "```Can you make them bigger?```\n-Minha",
        "```I'd like them bigger please.```\n-Minha",
        "```My favorite Kirby boss attack: ERASURE CANNON```\n-Minha",
        "```OFFICIAL LIAC DESIGNS MAKE ME BLEED FROM THE EYES AAAAAAAAAHHHHHHHHH```\n-Minha",
        "```I was introduced to FP via this shitty porn and all I got was this stupid trauma. And no T-shirt.```\n-Minha",
        "```You can't be a close friend of mine unless you've seriously hurt me emotionally and we managed to make it up after all. Three times.```\n-Minha",
        "```I'm going to the body shop to change the type of person I am!```\n-Minha",
        "```Wubba-lubba-dub-dub!```\n-Minha",
        "```Welcome to Ell-Eff-Arr's Cue An Ay! I'm Arr, and these are my co-hosts, Ell and Eff!```\n-Minha",
        "```Camel tax.```\n-Minha",
        "```I once won a prize for singing a song I hate sung by an artist I hate. At least I wasn't also hungover that year.```\n-Minha",
        "```Or the geckos ate them.```\n-Minha",
        "```...are you ignoring reality again?```\n-Minha",
        "```I can't approve of that.  's one of the few  characters I have zero qualms with. I wonder what I was trying to say there.```\n-Minha",
        "```Every day a new dream.```\n-Minha",
        "```You're just jealous because she's bigger in Pirate's Curse.```\n-Minha",
        "```It's like getting Michael Schumacher to complain about how you drive.```\n-Minha",
        "```ry. Sorry. Sorry. Sorry. Sorry. Sorry. Sorry. Sorry. Sorry. Sorry. Sorry. Sorry. Sor```\n-Minha",
        "```TELPROT!!111```\n-Minha",
        "```His mom has bigger legs.```\n-Minha",
        "```Iglooshrew.```\n-Minha",
        "```Stupid cat! I know you look more like a rat, but you're much bigger and stronger than me, aren't you? So that makes me the rat! And guess what? This rat has missiles! So eat missiles, you son of a bitch!```\n-Minha",
        "```I... guess I survived that?```\n-Minha",
        "```A PRINCIPAL WRESTLES A DEER```\n-Minha",
        "```METROID 2 PC IS THE BEST 2D METROID GAME THAT EVER EXISTED```\n-Minha",
        "```Rule 99: Nobody cares what horse you like, so don't talk about that.```\n-Minha",
        "```Mondatta Zenyatta Brothers!```\n-Minha",
        "```HIITO! ZEARU!```\n-Minha",
        "```but 2 da hed```\n-Minha",
        "```WHY IS IT ALWAYS BUSES FOR FUCK'S SAKE```\n-Minha"
        "```My cravings have nothing to do with reality!```\n-Minha",
        "```I'm in ur base stealin' ur waifus```\n-Minha"
        ]
        await self.bot.say(randchoice(minha))
        
    @commands.command()
    async def ig97quotes(self):
        """Italian Gamer and Italian Quotes""" 
        ig = ["```Can we just shut up about FP2 until it comes out? Jeez. It wouldn't kill ya to wait, you know.```\n-ItalianGamer97",
              "```For a moment, I thought Plom broke.```\n-ItalianGamer97",
              "```inb4 a where's that damn 4th sapphire shard joke```\n-ItalianGamer97",
              "```You know what would be fantastic? A type that kills Fairy-types without being weak to Ground.```\n-ItalianGamer97",
              "```Kraftwerk is one of my jams, man. Daft Punk is also cool.```\n-ItalianGamer97",
              "```Is it me, or is Maze starting to get a bit... I dunno... loopy?```\n-ItalianGamer97",
              "```I like the SegaSonic arcade game, but Wild Water Way can go suck it. It seems too damn easy to fall off of the platforms on the river near the end of the stage. Maybe it's because it's something with the trackball-to-analog stick-conversion. I don't even know.```\n-ItalianGamer97",
              "```I'd bet Dazl would like a rifle that shoots colorful bouncy balls that are also edible for some reason. And yes, that's a thing in GMod.```\n-ItalianGamer97",
              "```You know what's fun? Rifles that shoot colorful bouncy-and-somehow-edible balls. And that's a thing in Gmod.```\n-ItalianGamer97",
              "```You know what I like to do in Garry's Mod? Kill a bunch of hostile NPCs en masse with a wonderous variety of weapons.```\n-ItalianGamer97",
              "```You know what would make my day? SiivaGunner high-quality rips of Freedom Planet themes.```\n-ItalianGamer97",
              "```What if you take a pizza... and put it in a taco? That would be neat, as I've never really tried that before.```\n-ItalianGamer97",
              "```Maze... is an enigma that we may or may not ever understand.```\n-ItalianGamer97",
              "```Y'know, Minha freaked out over a rubbery-looking Lilac once.```\n-ItalianGamer97",
              "```I kinda-sorta love it that MN9's become a synonym for pizza.```\n-ItalianGamer97",
              "```Got pesky DNA Cannons bothering you? A fire bomb should do the trick! One hit and BAM, the thing's gone!```\n-ItalianGamer97",
              "```I like the SegaSonic arcade game, but Wild Water Way can go suck it. It seems too damn easy to fall off of the platforms on the river near the end of the stage. Mabye it's because it's something with the trackball-to-analog stick-conversion. I don't even know.```\n-ItalianGamer97",
              "```With politics these days, you'd have to choose the one who you'd think is less ass.```\n-ItalianGamer97",
              "```Okay, who's the wiseguy who put two adjacent springs in the middle of a cave?```\n-ItalianGamer97",
              "```I don't like it when there's a distinct lack of lipsync in a game. That was a thing that bothered me with MN9, by the way.```\n-ItalianGamer97",
              "```Mighty No. 9? I thought it was mediocre and a tad overly frustrating. The fact that the explosions kinda look like cheap-ass pizza didn't help. I also had no qualms against pirating it.```\n-ItalianGamer97",
              "```How come no one did the ayy lmao alien thing with Torque yet?```\n-ItalianGamer97",
              "```The moment you realize the purple hopping robot from Relic Maze looks a bit too much like a certain robot-obstacle-thing from ModNation Racers.```\n-ItalianGamer97",
              "```Is it me or does almost nobody like Torque? I personally digged his playstyle.```\n-ItalianGamer97",
              "```You know what I hate? Those little jumpin' shits from Sonic Triple Trouble's Atomic Destroyer Zone.```\n-ItalianGamer97",
              "```RNG's being a butt, eh?```\n-ItalianGamer97",
              "```Yeh, ya'd better run. But come back after a few minutes, mmkay? :v```\n-ItalianGamer97",
              "```I gotta say something worthy of being made into a command...```\n-ItalianGamer97, now a command.",
              "```Damn feminists ruining everything... >: (```\n-ItalianGamer97",
              "```50 bucks for a box? You could buy a new vidya game for about that price!```\n-ItalianGamer97",
              "```Please excuse me while I try to juggle puppies and bombs.```\n-ItalianGamer97"
              ]
        await self.bot.say(randchoice(ig))

    @commands.command()
    async def giga(self):
        """Salami the Multivitamin""" 
        giga = ["MMMMMMMMMMH :heart:","https://cdn.discordapp.com/attachments/173967012123377664/207128827971895296/unknown.png",
              "```I'm going to order some hot delicious mighty no 9```\n-GigaLem",
              "``` must I replace a silable in everyone's name with salt?```\n-GigaLem",
              "```It breaks my heart to see the puppy sad```\n-GigaLem",
              "```Boop da puppy's snoot```\n-GigaLem",
              "```my mother once said 'did you pack your fists in storage?' ```\n-GigaLem",
              "```there's barely any good nsfw art of the puppy, and none with big bouncies```\n-GigaLem",
              "```when doubt, pull out your -REDACTED FOR YOUNGISH AUDIENCES```\n-GigaLem",
              "```cyclone-tific progress goes boink```\n-GigaLem",
              "```green haired blue tunic = good lemmings,  norm of the North = bad lemmings```\n-GigaLem",
              "```Why must Comcast be hired by a bunch of monkeys?```\n-GigaLem",
              "```I'd throw Milla a bone -unzips pants-```\n-GigaLem",
              "```If it isn't the puppy I'm not c*mming.```\n-GigaLem",
              "```I mean that in a Google way```\n-GigaLem",
              "```at the time of this message, I still haven't beat Super Mario Bros, and you know why? BECAUSE I FUCKING HATE LAKITUS```\n-GigaLem",
              "```You can suck my brick```\n-GigaLem",
              "https://cdn.discordapp.com/attachments/219633993522348032/222174075475197953/unknown.png",
              "https://cdn.discordapp.com/attachments/192833044049166337/222916128282902528/FP_Dude.png",
              "https://cdn.discordapp.com/attachments/173967012123377664/224620968931229696/2016-09-11_02.55.58.png",
              "```Love is what?```\n-GigaLem",
              "```btw fuck fascination maxx```\n-GigaLem",
              "```Discount voice action!```\n-GigaLem",
              "```they're lucky that nipples mode turned off```\n-GigaLem",
              "```we're gonna knock out two stones with one bird...wait```\n-GigaLem",
              "https://cdn.discordapp.com/attachments/173967012123377664/227702671468003328/SkypePhoto_20160920_020755.jpg"
              "```I thought you were gonna put ketchup in the jello```\n-GigaLem",
              "```There are many ways to trigger gravity, one of them being the mere mention of lewd milla -shot in the head by graviy-```\n-GigaLem",
              "```bupper must poop that snoot.....that sounded better in my head```\n-GigaLem"
              ]
        await self.bot.say(randchoice(giga))

    @commands.command()
    async def sonic(self):
        """GOTTAGOFAST"""
        sonic = ["***YOU'RE TOO SLOW!***","Let's do it to it!","Hands off my chilli dogs!","Way past cool!","Catch you later, Eggman!"]
        await self.bot.say(randchoice(sonic))

    @commands.command()
    async def redquotes(self):
        """He's so cool he named himself after a guild of ninja assassins!"""
        redquotes = ["```now i'm just scrolling down to see if there's someone who thinks a non-downloadable guide is a good idea, but i haven't seen her name yet```\n-RedScarfUK",
                    "https://cdn.discordapp.com/attachments/205815814316752897/226806382958084096/unknown.png"]
        await self.bot.say(randchoice(redquotes))

    @commands.command()
    async def insult(self):
        """Sir, you're a smrrrrrr heeeeee!"""
        insult = ["https://www.youtube.com/watch?v=NPTIUxbgIBE"]
        await self.bot.say(randchoice(insult))

def setup(bot):
    bot.add_cog(randquotes(bot))

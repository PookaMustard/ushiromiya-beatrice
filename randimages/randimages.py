import discord
from discord.ext import commands
import random
from random import randint
from random import choice as randchoice
from discord.ext import commands
import datetime
import time
import aiohttp
import asyncio

class randimages:
    """Random images!"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def shion(self):
        """HAHAHAHAHAHAHAHAHAHAHA!"""
        chance = randint(1,100)
        if chance <= 75:
            return await self.bot.say('http://img1.ak.crunchyroll.com/i/spire2/fc24e1a77e12e1e0007185cd42e750541371546895_full.jpg')
        else:
            return await self.bot.say('http://images4.fanpop.com/image/photos/22700000/Shion-Sonozaki-sonozaki-fans-22705531-704-396.jpg')

    @commands.command()
    async def freiza(self):
        """This isn't even my final form!"""
        freiza = ["http://img-9gag-fun.9cache.com/photo/a9PmRPm_700b.jpg",
               "http://brain-images.cdn.dixons.com/0/9/20163490/l_20163490_001.jpg"]
        return await self.bot.say(randchoice(freiza))
        
    @commands.command()
    async def chatded(self):
        """Do not post ponies while it is dead."""
        chatded = ["https://cdn.discordapp.com/attachments/173967012123377664/198887286132310017/16sxn0.jpg",
               "https://cdn.discordapp.com/attachments/173967012123377664/198887289336758274/16sxna.jpg",
               "https://cdn.discordapp.com/attachments/173967012123377664/198887295238012932/16sxmt.jpg",
               "http://i.imgur.com/fP4BEOL.png"]
        return await self.bot.say(randchoice(chatded))
        
    @commands.command()
    async def zonic(self):
        """Zonic the...zonic?"""
        zonic = ["https://cdn.discordapp.com/attachments/173967012123377664/196798755712794625/Zonic_4_My_New_Life_Logo.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/196799830515908609/ZonicPresentsAlt.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/196799979094802433/ZonicIconLarge.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/196800304187047938/unknown.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/196800484332273666/unknown.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/196800747067670529/unknown.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/196800992803684353/mellorne_wallpaper.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/196801076781907969/OMEGANOTSERPENTINE.png",
               "```This is my Sonic OC Zonic. He haz tregic bakstory. His mum an dad wer kil in war so he tri to b kil on railroad tracks but doctors sewed leg on head cuz they coudnt find body. He listens to MCR and One Direction. He cri evryday for wut happen to him that day.```"]
        return await self.bot.say(randchoice(zonic))
        
    @commands.command()
    async def nope(self):
        """No. Just no."""
        nope = ["https://cdn.discordapp.com/attachments/173967012123377664/192449277249716226/Ck8hjiJUYAA9bKl.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/192450306016018433/ExtremeNope.gif",
               "http://i1.kym-cdn.com/photos/images/original/000/395/708/630.png",
               "http://i.imgur.com/vTTIoc6.gif",
               "https://cdn.meme.am/instances/65132365.jpg"]
        return await self.bot.say(randchoice(nope))
        
    @commands.command()
    async def bathingwithclothes(self):
        """Ever dreamed of bathing with your clothes on?"""
        bathclothed = ["http://i.imgur.com/FyUAAw0.png",
               "http://i.imgur.com/n74nqYR.png"]
        return await self.bot.say(randchoice(bathclothed))
        
    @commands.command()
    async def shantae(self):
        """Ever dreamed of censoring Shantae?"""
        chance = randint(1,100)
        if chance <= 95:
            return await self.bot.say('http://i.imgur.com/Fu0P8Zk.png')
        else:
            return await self.bot.say('http://i.imgur.com/E1ZVRnh.png')
            
    @commands.command()
    async def whatever(self):
        """Whatever."""
        squall = ["http://troll.me/images/squall/whatever-.jpg", "http://i.imgur.com/2EAAg.jpg",
                  "http://67.media.tumblr.com/2a90cd0b64a12ab64ae095134defeedc/tumblr_inline_mz1gj196vo1s3hvmd.jpg",
                  "http://i52.photobucket.com/albums/g12/Daghul/Squall-Whatever.jpg", "http://i.imgur.com/R7Azb.jpg",
                  "http://img10.deviantart.net/ef66/i/2011/157/e/5/squall_is_not_perturbed_by_meowchee-d3i9c8x.jpg",
                  "http://31.media.tumblr.com/20512ae88b365cc32e92ca169c523b8b/tumblr_mrj3jlIcCf1sfzmdbo2_250.gif",
                  "http://orig01.deviantart.net/7883/f/2015/301/7/c/squall_leonhart___united_states_of_whatever_by_eddiehimselfstolemyu-d9ennsg.jpg"
                 ]
        return await self.bot.say(randchoice(squall))
        
    @commands.command()
    async def chara(self):
        """Now this face is good. = )"""
        chance = randint(1,100)
        charachance = randint(1,1000)
        if chance <= 90:
            return await self.bot.say('=)\nhttp://imgur.com/download/DJGxtu7')
        else:
            if charachance <= 500:
                return await self.bot.say('=)\nhttp://imgur.com/download/DJGxtu7')
            elif charachance <= 750:
                return await self.bot.say(':)\nhttp://imgur.com/download/DqPfvHB')
            else:
                return await self.bot.say('https://images-1.discordapp.net/.eJwVx10OwiAMAOC7cABqt_KzXcY0DIGEyUKrL8a7G7-372Nes5vdVNVLdoCjSRrzsKJjcsm2jFF65quJTeMEVuVUz_xUAdxwCX7FiCFuK4VIsNzcf-S8jw4xEEF-t55F76nyZFvaw3x_44IlKg.u4gRjc9h4xSj0qE6LRLG_KtxQDA.gif')

    @commands.command()
    async def arahc(self):
        """) = .doog si ecaf siht woN"""
        chance = randint(1,100)
        charachance = randint(1,1000)
        if chance <= 90:
            return await self.bot.say('https://images-1.discordapp.net/.eJwVx10OwiAMAOC7cABqt_KzXcY0DIGEyUKrL8a7G7-372Nes5vdVNVLdoCjSRrzsKJjcsm2jFF65quJTeMEVuVUz_xUAdxwCX7FiCFuK4VIsNzcf-S8jw4xEEF-t55F76nyZFvaw3x_44IlKg.u4gRjc9h4xSj0qE6LRLG_KtxQDA.gif')
        else:
            if charachance <= 500:
                return await self.bot.say('https://images-1.discordapp.net/.eJwVx10OwiAMAOC7cABqt_KzXcY0DIGEyUKrL8a7G7-372Nes5vdVNVLdoCjSRrzsKJjcsm2jFF65quJTeMEVuVUz_xUAdxwCX7FiCFuK4VIsNzcf-S8jw4xEEF-t55F76nyZFvaw3x_44IlKg.u4gRjc9h4xSj0qE6LRLG_KtxQDA.gif')
            elif charachance <= 750:
                return await self.bot.say(':)\nhttp://imgur.com/download/DqPfvHB')
            else:
                return await self.bot.say('=)\nhttp://imgur.com/download/DJGxtu7')

    @commands.command()
    async def sakura(self):
        """Ever dreamed of being censored?"""
        sakura = ["http://i.imgur.com/96VNkgA.jpg",
               "http://i.imgur.com/5qGiZnog.jpg",
               "http://i.imgur.com/feyJTT8.jpg",
               "http://i.imgur.com/mvi028v.jpg"]
        return await self.bot.say(randchoice(sakura))
        
    @commands.command()
    async def salt(self):
        """Have salt?"""
        salt = ["http://vignette1.wikia.nocookie.net/kancolle/images/9/9a/Want_some_salt.jpg",
               "https://cdn.meme.am/instances/500x/55031607.jpg",
               "https://media.makeameme.org/created/well-then-you-q1b8n1.jpg"]
        return await self.bot.say(randchoice(salt))
        
    @commands.command()
    async def ovo(self):
        """Bingo!"""
        ovo = ["https://cdn.discordapp.com/attachments/173967012123377664/190571971564666881/Screen_Shot_2015-10-30_at_6.22.16_PM.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/190572657270456321/IMG_0670.jpg",
               "https://cdn.discordapp.com/attachments/173967012123377664/190607662881308683/Bingo_in_FP_CS_Icon_OvO.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/190607776324517890/BstayR_OvO.png",
               "https://cdn.discordapp.com/attachments/174342349458112512/201461860212408341/OvO-faced_Typhlosion.png",
               "https://cdn.discordapp.com/attachments/174342349458112512/202956906346708992/ovom.png",
               "=)\nhttps://cdn.discordapp.com/attachments/210904321720713217/228231840161464321/IMG_0401.JPG",
               "https://cdn.discordapp.com/attachments/225788942916517890/227603987841417216/IMG_0499.PNG",
               "https://cdn.discordapp.com/attachments/203898055232192512/229325805971308544/unknown.png",
               "https://cdn.discordapp.com/attachments/158028863513821186/230564256938983424/unknown.png",
               "https://cdn.discordapp.com/attachments/225788942916517890/231488839812644865/Alexia_OvO.png",
               "https://cdn.discordapp.com/attachments/225788942916517890/231489195934220290/Shelby_OvO.png"
               ]
        return await self.bot.say(randchoice(ovo))
        
    @commands.command()
    async def romanquotes(self):
        """Starring Roman!"""
        roman = ["https://cdn.discordapp.com/attachments/173967012123377664/202868725546745856/unknown.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/202868789149302785/unknown.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/202868857935888384/unknown.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/202868896527679489/unknown.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/202868948822261761/unknown.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/202868986071744512/unknown.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/202869014874161152/unknown.png",
               #"https://cdn.discordapp.com/attachments/173965999744221185/202873953377714178/unknown.png",
               "https://cdn.discordapp.com/attachments/178922264522260480/202874208160579584/unknown.png",
               "https://cdn.discordapp.com/attachments/189198110042488832/202874464210386945/unknown.png",
               "https://cdn.discordapp.com/attachments/173966944351944704/203594025494773770/unknown.png",
               "```he's not gainaxed, he's climaxed```\n-Roman",
               "```and to hide their growing dicks```\n-Roman, answering Plom"
               ]
        return await self.bot.say(randchoice(roman))
        
    @commands.command()
    async def friskface(self):
        """This face is overrated. -_-"""
        friskface = ["https://cdn.discordapp.com/attachments/173967012123377664/200813613718437890/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200814067529678849/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200815092084768769/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200815563201576962/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200814703885156353/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200818482143690753/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200819261101309953/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200819797540339714/frusk.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200820010338222081/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200821632611123203/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200822216810561538/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200824789227667458/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200826151411646466/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200826497731133441/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200827482180419585/unknown.png\n=)",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200828130267627521/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200829046626582529/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200829527960715266/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200830183924695042/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200830713556238347/unknown.png",
                     "https://cdn.discordapp.com/attachments/225788942916517890/231544812799524864/Technic_Frisk_Face.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200831279153938434/unknown.png",
                     "https://cdn.discordapp.com/attachments/173967012123377664/200831638467248129/unknown.png",
                     "http://imgur.com/download/DJGxtu7\nGreetings! I am Chara. What, you expected Frisk? He sold his soul to me. =)"]
        return await self.bot.say(randchoice(friskface))
        
    @commands.command(hidden=True)
    async def weegee(self):
        """Weegeesquare!"""
        weegee = ["https://lh6.googleusercontent.com/-dWUzHO0twIQ/V1n-efytS3I/AAAAAAAACUM/pPozGcXTDSIwdvhzRVQSoqJFq5v43jMzQCL0B/w48-h64-no/DLonk_idle_0.png",
               "https://lh6.googleusercontent.com/-O2H_nPtZ_lM/V1n-jhEoz9I/AAAAAAAACUM/WkewVrDQQcAWXJs2o2koF24gg2pWVBdYQCL0B/w88-h57-no/Weegee%2527s%2BRequest%252C%2Bwith%2Ba%2Btweak_20160319_190508.jpg",
               "https://lh5.googleusercontent.com/-7Lg4VvNReMA/V1n-kzsdwOI/AAAAAAAACUM/SupCobm8h5QP3_XCE0qc2_W6PKgq3L7gQCL0B/w47-h51-no/2_20160417_202903.jpg",
               "https://lh6.googleusercontent.com/-QEW_5_hdVj8/V1n-tSioO0I/AAAAAAAACUM/PYwEpkGMFLwjXU-RsebrZWgB1A3yND-vACL0B/s32-no/spr_Deb_0.png",
               "https://lh3.googleusercontent.com/-IjEvwALlGyg/V1n-zXJA5iI/AAAAAAAACUU/Li32CfrZ4oMl_cXBq8lPvXKcErZ8GsNuACL0B/w48-h50-no/spr_RyanBAS2_12.png",
               "https://lh4.googleusercontent.com/-XTDB0I2kUfQ/V2Xx0MwAsLI/AAAAAAAACZA/qz-zcVAmhvM_4cfKdjLmWHLaIDLG_pT2gCL0B/w42-h48-no/index.png",
               "https://lh4.googleusercontent.com/-xhxP7tqlxDk/V2Xytgvq_TI/AAAAAAAACZA/VyCpzLQ8oH0q63SnzPFxPGM760YjIrp4gCL0B/w48-h64-no/FDLonk_idle_0.png"]
        return await self.bot.say(randchoice(weegee))
        
    @commands.command()
    async def kfl(self):
        """Kentucky Fried Luigi!"""
        kfl = ["https://lh4.googleusercontent.com/-oexhXFIUcws/V1n---gChkI/AAAAAAAACUU/sAMqbgqIDrclqFldgu6vx25FAKyPQ_O0QCL0B/w48-h64-no/KFC_specN_3.png",
               "https://lh4.googleusercontent.com/-JD0NJULjAzg/V1n-8msS0_I/AAAAAAAACUU/SMUkD1JDxHQ-BKRz99Apg1m5YbTjFLdoQCL0B/w48-h64-no/KFC_specD_7.png"]
        return await self.bot.say(randchoice(kfl))
        
    @commands.command()
    async def bsod(self):
        """The Ultimate Screen."""
        bsod = ["http://f.fwallpapers.com/images/bsod-xp.jpg",
               "http://thewindowsclub.thewindowsclubco.netdna-cdn.com/wp-content/uploads/2015/09/Blue-Screen-of-Death-Windows-10.png"]
        return await self.bot.say(randchoice(bsod))

    @commands.command(pass_context=True)
    async def darules(self, ctx):
        """The loopholes are strong."""
        server = ctx.message.server
        await self.bot.say('http://vignette2.wikia.nocookie.net/fairlyoddparents/images/6/65/Abracatastrophe0793.jpg/revision/latest?cb=20160526203432&path-prefix=en')
        if server.id=='181225160622342144':
            await self.bot.say('Check server rules in ' + '<#181228813982760960>' +'!')
        elif server.id=='173965999744221185':
            await self.bot.say('Check server rules in ' + '<#214420278334193665>' +'!')
        elif server.id=='205058315577851904':
            await self.bot.say('Check server rules in ' + '<#205058315577851904>' +'!')

    @commands.command(pass_context=True)
    async def elrules(self, ctx):
        """The loopholes are sexy. And Spanish."""
        server = ctx.message.server
        await self.bot.say('http://vignette4.wikia.nocookie.net/fairlyoddparents/images/9/99/FairyFairyQuiteContrary094.jpg/revision/latest?cb=20110404231200&path-prefix=en')
        if server.id=='181225160622342144':
            await self.bot.say('Consultar las reglas del servidor en ' + '<#181228813982760960>' +'!')
        elif server.id=='173965999744221185':
            await self.bot.say('Consultar las reglas del servidor en ' + '<#214420278334193665>' +'!')
        elif server.id=='205058315577851904':
            await self.bot.say('Consultar las reglas del servidor en ' + '<#205058315577851904>' +'!')

    @commands.command()
    async def lilac(self):
        """She's a dragon dragon."""
        await self.bot.say('http://vignette3.wikia.nocookie.net/freedomplanet/images/0/05/Lilac_Sketch_by_Stephen_DiDuro.png/revision/latest?cb=20140803235415')
        
    @commands.command()
    async def carol(self):
        """She's a wildcat wildcat."""
        await self.bot.say('http://vignette4.wikia.nocookie.net/freedomplanet/images/a/a7/Carol_Sketch_by_Stephen_DiDuro.jpg/revision/latest?cb=20140805001110')
        
    @commands.command()
    async def milla(self):
        """She's a dog dog."""
        await self.bot.say('http://vignette1.wikia.nocookie.net/freedomplanet/images/9/90/Milla_Basset_Sketch_by_Stephen_DiDuro.png/revision/latest?cb=20140805001350')
        
    @commands.command()
    async def galacticstumpy(self):
        """I wish Freedom Planet died already."""
        await self.bot.say('https://cdn.discordapp.com/attachments/192817084789424128/222898339648110592/GalacticStumpy.png')
        
    @commands.command()
    async def captainfalcon(self):
        """How about showing his moves?"""
        await self.bot.say('https://media.giphy.com/media/vl2wBbQc5t4as/giphy.gif')
        
    @commands.command()
    async def ontheedge(self):
        """Off the edge."""
        await self.bot.say('http://forums.sonicretro.org/uploads/av-4869.png')
        
    @commands.command()
    async def trump(self):
        """MAKE AMERICA GREAT AGAIN, the cool way."""
        await self.bot.say('http://i.imgur.com/hKeuu64.jpg')
        
    @commands.command()
    async def samus(self):
        """Smooth Bounty Hunter."""
        await self.bot.say('http://i3.photobucket.com/albums/y89/CX-Neo/samus_jackson_by_benjamin_matthews-d353ekn.gif')    
    
    @commands.command()
    async def mouse(self):
        """Mouse issues."""
        await self.bot.say('http://static.zerochan.net/Nazrin.full.831987.jpg')
        
    @commands.command()
    async def graphics(self):
        """The stupidity of graphics arguments"""
        await self.bot.say('http://i.imgur.com/5m3zGue.jpg')
        
    @commands.command()
    async def soapbox(self):
        """Like ACME! But with soap."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/193922258937446412/soapbox.gif')
        
    @commands.command()
    async def draam(self):
        """Use when drama intensify."""
        await self.bot.say('https://cdn.discordapp.com/attachments/190590897480663040/222143396116955142/unknown.png')
        
    @commands.command()
    async def kidding(self):
        """Are you kidding?"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/195207061271740417/You-Have-Got-To-Be-Kidding-Me-GIF.gif')
        
    @commands.command()
    async def physics(self):
        """Laws of physics destroyed."""
        physics = ["http://i158.photobucket.com/albums/t83/sirtmagus2/THE%20FUTURE/sonic4whoops.jpg",
                   "http://i1.kym-cdn.com/photos/images/original/000/910/238/8dc.png"]
        await self.bot.say(randchoice(physics))
        
    @commands.command()
    async def gottagofast(self):
        """Or else be left behind!!"""
        fast = ["http://orig12.deviantart.net/4ae4/f/2011/348/7/1/gotta_go_fast_by_zeurel-d4j3lie.gif",
                   "http://orig07.deviantart.net/d3a5/f/2011/357/b/3/gota_go_fsat_sanic_by_kynquinhe-d4jyyd5.gif"]
        await self.bot.say(randchoice(fast))
        
    @commands.command()
    async def sanic(self):
        """Fastest thing alive! SAAANIC!"""
        await self.bot.say("http://orig04.deviantart.net/1239/f/2015/186/7/e/oh_sanic_by_reborngamergirl-d8zzixx.gif")
        
    @commands.command()
    async def dinkleberg(self):
        """Mr. Turner...!!!"""
        await self.bot.say("http://img01.deviantart.net/4bef/i/2013/008/3/a/dinkleberg__by_akari_61-d5qwvqg.jpg")
        
    @commands.command()
    async def mfw(self):
        """It's not really my face though."""
        mfw = ["https://cdn.discordapp.com/attachments/173967012123377664/200676850446499841/unknown.png",
                   "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQXg8VU_dEl-z_CwyLHF6QtOoaJJbyS7UBGjCsSJ2b4seE4N5Py"]
        await self.bot.say(randchoice(mfw))
        
    @commands.command()
    async def delete(self):
        """Deletes this command when used."""
        delete = ["http://img13.deviantart.net/c4bb/i/2015/120/9/a/cybermen__quot_delete_quot__campaign_by_degaspiv-d33hjoa.png",
                   "http://i0.kym-cdn.com/photos/images/facebook/001/107/323/dbb.jpg",
                   "http://i0.kym-cdn.com/news_feeds/icons/mobile/000/020/528/fa1.jpg",
                   "https://s-media-cache-ak0.pinimg.com/236x/51/0f/a8/510fa8e2a1874b4916f6ab42d3affabd.jpg",
                   "https://www.ponychan.net/site/src/1454799320298.png",
                   "http://i3.kym-cdn.com/photos/images/newsfeed/001/146/898/c9c.jpg",
                   "http://i3.kym-cdn.com/photos/images/newsfeed/001/149/437/656.jpeg",
                   "https://cdn.discordapp.com/attachments/205815814316752897/216534126524760074/DeleteThisMetroid.png",
                   "https://cdn.discordapp.com/attachments/173967012123377664/218060287289327616/HowAboutADELETETHIS.PNG"]
        await self.bot.say(randchoice(delete))
        
    @commands.command()
    async def grandad(self):
        """Or grandmother. I don't care anymore."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/198976315930574849/a3173909832_10.jpg')
        
    @commands.command()
    async def idonteven(self):
        """I. Don't. Even."""
        await self.bot.say('http://images.akamai.steamusercontent.com/ugc/268342479504771643/3053D7EC4642AE3FD2B024785B4DFD501579F730/')
        
    @commands.command()
    async def twobecomeone(self):
        """VVVVVV strikes back!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/198542992640835585/Two_Viridians_Become_One.png')
        
    @commands.command()
    async def popular(self):
        """Run away from the popularity!!"""
        await self.bot.say('https://a.dilcdn.com/bl/wp-content/uploads/sites/25/2015/03/Jack-Sparrow-Life-Goals-5.jpg')
        
    @commands.command()
    async def roystory(self):
        """No, no Bowsers for you."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/194954164445511681/IMG_24082015_215738.png')
        
    @commands.command()
    async def thumbsup(self):
        """Going overboard, aren't we?"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/193897410664202241/Megalike.gif')
        
    @commands.command()
    async def solomon(self):
        """Nuking an entire waship fleet? Cool!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/196081496132550657/GP02_Nuke_3.gif')

    @commands.command()
    async def supernova(self):
        """Nuking an entire solar system? EVEN COOLER!"""
        await self.bot.say('http://i.makeagif.com/media/6-30-2016/nvigN6.gif')
        
    @commands.command()
    async def shipshippingships(self):
        """A ship shipping ship shipping shipping ships."""
        await self.bot.say('http://funnyasduck.net/wp-content/uploads/2013/02/funny-ship-shipping-ships-pics.jpg')
        
    @commands.command()
    async def peashy(self):
        """She's not the PC. She's the TurboGrafx 16."""
        await self.bot.say('http://i.imgur.com/HGGnD03.jpg')
        
    @commands.command()
    async def frisk(self):
        """My face is better and more energetic. -_-"""
        await self.bot.say('-_-\nhttp://imgur.com/download/SBK02Zy')
        
    @commands.command()
    async def biggaydance(self):
        """Uhh..."""
        await self.bot.say('http://31.media.tumblr.com/4ea7b737b18ede28490a28a41e2c3f19/tumblr_mp8icf6PhR1s83bdoo2_400.gif')
        
    @commands.command()
    async def popcorn(self):
        """The heat is intensifying!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/196313267939966978/Popcorn.gif')
        
    @commands.command()
    async def headcanon(self):
        """It's a head canon."""
        await self.bot.say('http://img4.wikia.nocookie.net/__cb20130704181437/ishipit/images/f/f7/Headcanon.jpg')
        
    @commands.command()
    async def nooo(self):
        """PADME!!!!!!!!!"""
        await self.bot.say('http://www.nooooooooooooooo.com/vader.jpg')    
        
    @commands.command()
    async def no(self):
        """Undramatic!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/170551952063594497/212916613249368064/IMG_20160810_080216.jpg')
        
    @commands.command()
    async def animeisdisgusting(self):
        """Very disgusting."""
        await self.bot.say('http://img.memecdn.com/this-post-is-so-triggering-to-weebs-everywhere-shame-on-you-anita_fb_6581597.jpg')    
        
    @commands.command()
    async def yup(self):
        """Our plan will come to fruitition..."""
        await self.bot.say('http://i.imgur.com/JB8VEA9.gif') 
        
    @commands.command()
    async def metashoe(self):
        """The shoe of a meta knight."""
        await self.bot.say('http://orig15.deviantart.net/9a5f/f/2011/308/e/9/kirby___the_meta_shoe_by_minon-d4f2bt1.png')
        
    @commands.command()
    async def shark(self):
        """Cliche shark movies. Not?"""
        await self.bot.say('https://images-ext-2.discordapp.net/eyJ1cmwiOiJodHRwOi8vaTMua3ltLWNkbi5jb20vcGhvdG9zL2ltYWdlcy9uZXdzZmVlZC8wMDEvMTU0LzM3OC9kYWIuZ2lmIn0.5b03lJNfumY4RbDn6kqQ3aP9E7I.gif')
        
    @commands.command()
    async def triggered(self):
        """IT'S NO USE!"""
        trig = ["https://cdn.discordapp.com/attachments/173967012123377664/209860253033037825/chompistriggered.gif",
                "https://cdn.discordapp.com/attachments/173967012123377664/196825883024031747/2c4.png",
                "https://pbs.twimg.com/media/CpCiJHhW8AApLCL.jpg",
                "https://i.ytimg.com/vi/0Ny-nC3LBWk/hqdefault.jpg"]
        await self.bot.say(randchoice(trig))
        
    @commands.command()
    async def shitstorm(self):
        """The calm before the typhoon."""
        trig = ["http://i2.kym-cdn.com/photos/images/facebook/000/358/764/bb0.png",
                "http://i2.kym-cdn.com/photos/images/facebook/000/091/829/8b1.png"]
        await self.bot.say(randchoice(trig))
        
    @commands.command()
    async def second(self):
        """First, then Second."""
        await self.bot.say('https://i.imgur.com/7lWjDiH.png')
        
    @commands.command()
    async def firefox(self):
        """Internet browsing just got hotter."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/196994416907386881/Hannameme.png')

    @commands.command()
    async def bored(self):
        """Another Freedom Planet command, ugh."""
        await self.bot.say('https://cdn.discordapp.com/attachments/189389254093307905/196083185438687233/Bored.PNG')
        
    @commands.command()
    async def justright(self):
        """Very right."""
        await self.bot.say('http://i2.kym-cdn.com/photos/images/facebook/001/070/061/d96.jpg')
        
    @commands.command()
    async def friend(self):
        """With Kirby."""
        await self.bot.say('http://img13.deviantart.net/5363/i/2014/273/c/8/kirby_is_shaped_like_a_friend_by_triple_q-d80v31j.jpg')
        
    @commands.command()
    async def coincidence(self):
        """I think not."""
        await self.bot.say('https://cdn.discordapp.com/attachments/172006506525360129/197429850074644482/PhijPZB.gif')
        
    @commands.command()
    async def yeolder(self):
        """I think not."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/197714935319494657/Screenshot_2016-06-29-07-08-04.png')
        
    @commands.command()
    async def okay(self):
        """I approve of this."""
        await self.bot.say('http://i.makeagif.com/media/10-04-2015/f0UVsa.gif')
        
    @commands.command()
    async def mettaton(self):
        """OH YEAHHHH!"""
        await self.bot.say('https://66.media.tumblr.com/b37f1c1e0d96623dbd7d52f3f4be8bd6/tumblr_nwsnqumBLA1tohl7eo1_400.gif')
        
    @commands.command()
    async def puru(self):
        """Japanese stuff..."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192355333035786242/PuruProtocultureJoke.PNG')
        
    @commands.command()
    async def rekt(self):
        """Poor stormtrooper..."""
        await self.bot.say('http://i.imgur.com/9sKSRFD.gifv')

    @commands.command()
    async def yay(self):
        """I love it!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/192751917770866689/Yay.gif')
 
    @commands.command()
    async def niccage(self):
        """Featuring Nicolas Cage!"""
        await self.bot.say('https://i.ytimg.com/vi/G8GVWhviw8s/hqdefault.jpg') 
        
    @commands.command()
    async def youwin(self):
        """A WINNER IS YOU!"""
        await self.bot.say("http://www.glorioustrainwrecks.com/files/screens/YOU'RE%20WINNER.png") 
        
    @commands.command()
    async def roystory(self):
        """Definitely not about Roy."""
        await self.bot.say("https://images-1.discordapp.net/.eJwFwdENhCAMANBdGIBC7WF1G4INelFLoH6Z2_3ee93TT7e63ayNFWA7RtG--WHacxVfVespuR3DF70gm-WyX3LbgEgYpjnSB1PCJSRmQIxMIU1MM8UlMDGULP7bpLrfH5tgIVc.8_YfgaQw6qDLJhNoRX81B_8lOXM.jpeg")
        
    @commands.command()
    async def facebook(self):
        """By that I mean a book to the face."""
        await self.bot.say("http://www.meh.ro/wp-content/uploads/2012/02/meh.ro9248.png") 
        
    @commands.command()
    async def uvu(self):
        """happy"""
        await self.bot.say("http://media.tumblr.com/tumblr_mckacmNq3G1rvydwz.png") 
        
    @commands.command()
    async def genuineanger(self):
        """This Heavy item goes for $200 on the TF2 shop"""
        await self.bot.say("http://i3.kym-cdn.com/photos/images/facebook/001/111/746/a32.jpg") 
        
    @commands.command()
    async def irony(self):
        """It's hot."""
        await self.bot.say("https://cdn.discordapp.com/attachments/130541134760902656/218862634630381568/Oh_The_Irony.jpg") 
        
    @commands.command()
    async def sharing(self):
        """Sharing is caring."""
        sharing = ["https://cdn.discordapp.com/attachments/167706685715120129/218413739844698122/The.Pirate.Bay.Cartoon-small.png",
                   "https://cdn.discordapp.com/attachments/167706685715120129/218839570492424194/sharing.jpg"
                  ]
        await self.bot.say(randchoice(sharing)) 
        
    @commands.command()
    async def tobecontinued(self):
        """Coming Soon!"""
        await self.bot.say('https://img0.etsystatic.com/059/0/10858326/il_570xN.762412812_ccx3.jpg')    
        
    @commands.command()
    async def escalated(self):
        """Escalators are fun. Also boring."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/193499284899889153/b93f0e354df1d3a803f8e47adaae7651.png')    
        
    @commands.command()
    async def zerosystem(self):
        """Startup initiation commence!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/189389254093307905/191661403596259330/tumblr_zerosystem.gif')
        
    @commands.command()
    async def examwarning(self):
        """Beware the exam!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192311643969945601/EXAM_System_-_Activated.jpg')

    @commands.command()
    async def android(self):
        """THE Google Android"""
        await self.bot.say('http://crackberry.com/sites/crackberry.com/files/styles/large/public/topic_images/2013/ANDROID.png?itok=xhm7jaxS')
        
    @commands.command()
    async def tumbleweed(self):
        """Pure abandonement."""
        await self.bot.say('https://brittnyhabibti.files.wordpress.com/2014/10/tumbleweed.jpg')
        
    @commands.command()
    async def lordstrife(self):
        """Two abominations merged into one."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/224702731846156288/Lord_Strife.png')

    @commands.command()
    async def lenny(self):
        """Pure elaborate faces."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/212743476285145098/Screenshot_291.png')
        
    @commands.command()
    async def ihavethepower(self):
        """You have the power!!!!"""
        await self.bot.say('http://s2.quickmeme.com/img/70/7028dd710bc900a57fb7068e7c1f968ce67db1ff908a709ae53ac888bf245ce7.jpg')
        
    @commands.command()
    async def headdesk(self):
        """When the fail is even stronger."""
        headdesk = ["http://i.giphy.com/JRMvrNMKfjqmI.gif", "https://cdn.discordapp.com/attachments/173965999744221185/192431766726901761/Headdesk_Violent.gif"]
        await self.bot.say(randchoice(headdesk))
        
    @commands.command()
    async def burnheal(self):
        """You're going to need it."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192432102313164801/4313739.png')
        
    @commands.command()
    async def whysoserious(self):
        """Why not be funny, in a murderous way?"""
        await self.bot.say('http://orig12.deviantart.net/6f85/f/2008/201/b/b/why_so_serious__by_tyrite.jpg')
        
    @commands.command()
    async def spoileralert(self):
        """Massive spoilers incoming!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192432214238167042/Spoiler_Alert.jpg')
        
    @commands.command()
    async def supertorque(self):
        """He's a super alien alien."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192432139415977985/IMG_16052016_111115.png')
        
    @commands.command()
    async def technicallycorrect(self):
        """Correctly correct!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192432893694443522/TBKOC.jpg')
        
    @commands.command()
    async def ironysales(self):
        """A  sale? That's cute..."""
        await self.bot.say('http://ci.memecdn.com/125/9837125.jpg')
        
    @commands.command()
    async def bananaears(self):
        """Bananas for your ears."""
        await self.bot.say('https://cdn.discordapp.com/attachments/196713723182710784/211582717060579328/creationist_asshole.gif')
        
    @commands.command()
    async def exeggutor(self):
        """You're dimma-tall!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/211648917480144896/CpBhDz5UIAAwS1d.png')
        
    @commands.command(hidden=True)
    async def cloudi(self):
        """Cloudi"""
        await self.bot.say('https://lh3.googleusercontent.com/-HsnLVgWSasQ/V2Xyubme1EI/AAAAAAAACZA/Cbhh03dC2XAvssfU220auatYS_I8MoGewCL0B/w96-h64-no/spr_credits_3.png')
        
    @commands.command()
    async def steamnazis(self):
        """Steam in a nutshell."""
        await self.bot.say('https://cdn.discordapp.com/attachments/178247098737754133/189429160525955073/aynA4ZY_700b_v1.jpg')
        
    @commands.command()
    async def dealwithit(self):
        """Cool glasses."""
        await self.bot.say('http://imgur.com/HuoQG53')
        
    @commands.command()
    async def pokerface(self):
        """Your tension is about to lower."""
        await self.bot.say('https://cdn.discordapp.com/attachments/196051622055378953/233266445671202816/unknown.png')
        
    @commands.command()
    async def hammer(self):
        """Your life ends thirty minutes from now."""
        await self.bot.say('https://cdn.discordapp.com/attachments/196051622055378953/233321606124929024/unknown.png')
        
    @commands.command()
    async def wat(self):
        """Huh"""
        await self.bot.say('http://i.ytimg.com/vi/hEfa0C897H4/maxresdefault.jpg')
        
    @commands.command()
    async def waa(self):
        """It's time to cry"""
        await self.bot.say('http://i.imgur.com/gJgoKdK.gifv')
        
    @commands.command()
    async def gottam(self):
        """Eyes are going to pop out hard"""
        await self.bot.say('https://cdn.discordapp.com/attachments/228634072572887040/231191724561661966/Engie.png')
        
    @commands.command()
    async def sadneptune(self):
        """Neptune is sad."""
        await self.bot.say('`You managed to make NEPTUNE sad! How could you even...`\nhttps://cdn.discordapp.com/attachments/196051622055378953/231935403974852609/IMG_1197.PNG')
        
    @commands.command()
    async def objection(self):
        """Cool pose."""
        await self.bot.say('https://cdn.discordapp.com/attachments/167706685715120129/189796749420789763/objection.jpg')
        
    @commands.command()
    async def vert(self):
        """Censorship has gone extreme."""
        await self.bot.say('http://i.imgur.com/8919cM8.jpg')     
        
    @commands.command()
    async def noire(self):
        """Who's next to bite the dust?"""
        await self.bot.say('http://i.imgur.com/DxHitLz.jpg') 
        
    @commands.command()
    async def steamguard(self):
        """Ineffective solutions invade!"""
        await self.bot.say('https://cdn.discordapp.com/attachments/172006506525360129/199185289372106754/the_most_useless_things_you_will_ever_see_640_02.jpg')

    @commands.command()
    async def youdied(self):
        """Back to Dark Souls."""
        await self.bot.say("http://img4.wikia.nocookie.net/__cb20130515050459/darksouls/images/6/63/You-Died.jpg")
        
    @commands.command()
    async def aerisisdead(self):
        """SPOILER ALERT! And I don't care about 'Aerith'."""
        await self.bot.say("https://geekgirlmagazine.files.wordpress.com/2012/02/aeris-death.jpg")
        
    @commands.command()
    async def mlp(self):
        """Friendship is Magic!"""
        spoilers = ["https://geekgirlmagazine.files.wordpress.com/2012/02/aeris-death.jpg\nIn *Final Fantasy VII*, Aeris(th) dies with no return.",
                    "http://cloud-3.steamusercontent.com/ugc/613919720080121549/1FC6871EC21CFF7C1F325214BE973F8AF04B0944/\nIn *Eversion*, you learn in the good ending that Zee Tee was an eldritch abomination all along.",
                    "http://66.media.tumblr.com/ee844a8777ca03043d52ae6b39b5c85a/tumblr_mz0exoZCpm1tn5y1lo4_250.gif\nIn *Final Fantasy VIII*, you learn that Sorceress Edea used to be the Matron of the party, hence why Irvine was reluctant to kill her. And that the big bad is Sorceress Ultimecia.\nhttp://vignette2.wikia.nocookie.net/p__/images/3/34/Cid_and_Edea_Kramer.png/revision/latest?cb=20140704104304&path-prefix=protagonist\nAlso, you learn that she was the wife of Cid.",
                    "https://images-2.gog.com/1c53ba37fb09f2ef0484fa28e833ca0f1e15cfc24abf55a59bfac36faaee1874.png\nIn *Undertale*, you learn that:\n-Flowey used to be Asriel Dreemurr\n-Chara (or whatever you name them) is the personification of a power hungry player\n-Your human player is called Frisk\n-Alphys experimented on live monsters, resulting in the Amalgamates\n-LV means Level of Violence and EXP means Execution Points\n-Asgore is not evil, and he doesn't want power. He even hates killing the humans\n-Chara died to buttercup poisoning\n-Asriel died due to getting attacked from the humans\n-Asriel was struggling in control with Chara when their souls combined",
                    "http://vignette1.wikia.nocookie.net/assassinscreed/images/2/2b/Al_Mualim_controling_Altair.png\nIn *Assassin's Creed*, you learn that Al-Maulim has betrayed you and is using the power of the Apple of Eden for mind control. And he is a templar.",
                    "http://static.trueachievements.com/customimages/023853.jpg\nContrary to what you believe, in *Portal 2*, Wheatley is the final boss. He will betray you and then attempt to kill you.",
                    "http://img2.wikia.nocookie.net/__cb20130403193441/sonic/images/a/ab/Time_Eater_Full_Appearance.png\nIn *Sonic Generations*, Classic AND Modern Eggman take control of the Time Eater to give you the final boss of the game.",
                    "http://67.media.tumblr.com/4a9676d2b62d5e9c4603f81d82acd2a3/tumblr_nh296yGCAe1rawb5do1_500.png\nIn *Alice Madness Returs*, Alice's cat didn't burn her house. Dr. Bumby did."
                    ]
        await self.bot.say(randchoice(spoilers))
        
    @commands.command()
    async def wrong(self):
        """xkcd levels of wrong."""
        await self.bot.say("https://imgs.xkcd.com/comics/duty_calls.png")

    @commands.command()
    async def jojo(self):
        """Move out."""
        await self.bot.say("http://i.imgur.com/2f19khz.gif")
        
    @commands.command()
    async def confoundthem(self):
        """Don't drink THAT much!"""
        await self.bot.say("http://imgur.com/wDKwqN0")

    @commands.command()
    async def iamyourfather(self):
        """The Father Strikes Back."""
        await self.bot.say("http://i.perezhilton.com/wp-content/uploads/2015/11/star-wars-empire-strikes-back-movie-misquote.gif")

    @commands.command()
    async def rip(self):
        """Rest in Peace."""
        await self.bot.say("http://www.spokeo.com/blog/wp-content/uploads/2011/05/RIP-Spokeo-Info-Bubble.jpg")
        
    @commands.command()
    async def bedtime(self):
        """Do you want to have a bad time?"""
        await self.bot.say("https://cdn.discordapp.com/attachments/174285836475564032/222962866230263818/unknown.png")
        
    @commands.command()
    async def undersans(self):
        """(comic sans font): undertale sans"""
        sans = ["http://i2.kym-cdn.com/photos/images/newsfeed/001/021/889/68d.gif", "https://pbs.twimg.com/media/ClvCNZVUkAA3uWA.jpg",
                "https://images-1.discordapp.net/.eJwNwlEOgyAMANC7cAAqRQS9zNIgQTOlhHZfy-4-X97XfMZlNnOodtkA9lMyj92K8qBabGWuV6F-is18A6lSPu7SVACnkNxz9m6JAdMaAd2ECcOafPQB_RwiCDV58dv2Vs3vDwY2IsA.qdTbn0mCDjJYLQxOSY2w5lDD6e0.png?width=400&height=118"]
        await self.bot.say(randchoice(sans))
        
    @commands.command()
    async def toriel(self):
        """The Caretaker of the Ruins"""
        gettutorials = ["http://i.imgur.com/U84yd9d.png", "http://i.imgur.com/tiqY2on.png", "http://i.imgur.com/FZRwh86.png"]
        await self.bot.say(randchoice(gettutorials))
        
    @commands.command()
    async def flowey(self):
        """In this world, it's KILL or be KILLED. I think..."""
        flowey = ["http://i.imgur.com/66t5QUc.jpg"]
        await self.bot.say(randchoice(flowey))
        
    @commands.command()
    async def asriel(self):
        """In this world, it's SHRUG or be SHRUGGED. Ho?"""
        asriel = ["https://67.media.tumblr.com/853f0b2013920b1a660115d538cf83f3/tumblr_nvwaot5Q861r9xrggo3_400.gif"]
        await self.bot.say(randchoice(asriel))
        
    @commands.command()
    async def nomercy(self):
        """Bye, MERCY button!"""
        nomercy = ["http://i.makeagif.com/media/11-22-2015/F2Q8G0.gif"]
        await self.bot.say(randchoice(nomercy)) 
        
    @commands.command()
    async def asgore(self):
        """Howdy! Want to have some tea?"""
        asgore = ["http://vignette2.wikia.nocookie.net/undertale/images/f/f1/Untitled-3.png/revision/latest?cb=20151228183442"]
        await self.bot.say(randchoice(asgore)) 
        
    @commands.command()
    async def papyrus(self):
        """(PAPYRUS FONT): UNDERTALE PAPYRUS"""
        pap = ["https://images-2.discordapp.net/.eJwVx9sNgCAMAMBdGIAWVHws4QwECZqoJbT6Y9xdTO7nHnWVXU1qFck8ASwbByqLZqHiU9SJKO3R5411oAO8iA_rEU9hML1FdF1lu8ahsSNYHFo3mNpf7xBhvmedz6TeD3e2IM8.9CW2o13A9Lm0mQp_HbONhp-igtc.png"]
        await self.bot.say(randchoice(pap))
        
    @commands.command()
    async def getdunkedon(self):
        """(comic sans font): what it says"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173965999744221185/195698701904117761/sansdunk.png")
        
    @commands.command()
    async def saltae(self):
        """What do you call an angry half-genie?"""
        await self.bot.say("http://i.imgur.com/dGOfP7L.png")
        
    @commands.command()
    async def nopower(self):
        """You have no power here."""
        await self.bot.say("http://i1.kym-cdn.com/photos/images/original/000/913/758/a12.jpg")
        
    @commands.command()
    async def areyoukiddingme(self):
        """Say what?!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/165012316402745344/211553360027975682/IMG_3355.PNG")
        
    @commands.command()
    async def romanabominations(self):
        """Abominations by Roman!"""
        roab = ["https://cdn.discordapp.com/attachments/173966944351944704/209431917378928640/unknown.png"]
        await self.bot.say(randchoice(roab))
        
    @commands.command()
    async def poke(self):
        """Do not poke the Not!Mew"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/207593380937596928/unknown.png")
        
    @commands.command()
    async def puppy(self):
        """Mood Milla"""
        puppy = ["http://i.imgur.com/mnI1tkU.png",
                "https://cdn.discordapp.com/attachments/203898055232192512/204015895519952896/unknown.png",
                "https://cdn.discordapp.com/attachments/174342349458112512/207727604671840257/Milla_Full-body_-_v1.0.png",
                "https://cdn.discordapp.com/attachments/192817084789424128/220363274774904832/milla_i_dont_know.png",
                "https://art.risingslash.net/_images/1cd531178f9ccc250513c74d4d1dcc4d"]
        await self.bot.say(randchoice(puppy))
        
    @commands.command()
    async def plom(self):
        """..."""
        await self.bot.say("https://cdn.discordapp.com/attachments/189198110042488832/202902488897028096/unknown.png")
        
    @commands.command()
    async def error(self):
        """Teleporting...bread?"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/202441867575427072/unknown.png")
        
    @commands.command()
    async def shitgetsreal(self):
        """You don't want to be involved."""
        await self.bot.say("http://images.akamai.steamusercontent.com/ugc/1613797962856652704/A8CE21DDA6B488764514BD502EB88014F7892A18/")
        
    @commands.command()
    async def sadbingo(self):
        """Ever heard of sad multivas?"""
        await self.bot.say("https://cdn.discordapp.com/attachments/189888913668571146/208350639850258432/unknown.png")
        
    @commands.command()
    async def iseeit(self):
        """What you did there."""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/195342207526502401/WYDTISI.png")
        
    @commands.command()
    async def smug(self):
        """Smugging hard."""
        await self.bot.say("https://cdn.discordapp.com/attachments/184816492838256640/190986742227009538/IMG_0291.JPG")
        
    @commands.command()
    async def disgust(self):
        """You are very disgusted."""
        await self.bot.say("https://cdn.discordapp.com/attachments/196051622055378953/210878832012558336/IMG_0494.JPG")
        
    @commands.command()
    async def smugmode(self):
        """Smugging harder."""
        await self.bot.say("https://v.dreamwidth.org/27224/52508")
        
    @commands.command()
    async def owtheedge(self):
        """So edgy. I love it."""
        await self.bot.say("http://i.imgur.com/2Yni481.jpg")
        
    @commands.command()
    async def promotion(self):
        """Have one! Not?"""
        await self.bot.say("http://stream1.gifsoup.com/view1/3156672/robotnik-prrrromotion-o.gif")
        
    @commands.command()
    async def burn(self):
        """It burns!"""
        burn = ["http://ci.memecdn.com/566/824566.jpg", "https://memecrunch.com/meme/214GL/picard-burn/image.png?w=500&c=1"]
        await self.bot.say(randchoice(burn))
        
    @commands.command()
    async def muda(self):
        """Another anime punch GIF."""
        await self.bot.say("http://imgur.com/6zcE2Vz")
        
    @commands.command()
    async def zawarudo(self):
        """Flashing images. Please consult your doctor."""
        await self.bot.say("http://38.media.tumblr.com/c2d4006f53aa908b6de083ee4a7672d3/tumblr_n5xz2qbEmM1r6mrcio3_250.gif")

    @commands.command()
    async def barvon(self):
        """Duke Arktivus Barvon at your service."""
        await self.bot.say("https://cdn.discordapp.com/attachments/173965999744221185/192621822108237825/barvon.png")

    @commands.command()
    async def facepalm(self):
        """When the fail is strong enough."""
        await self.bot.say("http://i.imgur.com/iWKad22.jpg")

    @commands.command()
    async def doublefacepalm(self):
        """When the fail is even stronger."""
        await self.bot.say("http://robinbrown.co.uk/wp-content/uploads/2012/02/double-facepalm1.jpg")

    @commands.command()
    async def quadfacepalm(self):
        """When the fail is stronger than ever."""
        await self.bot.say("https://cdn.discordapp.com/attachments/225788942916517890/233190758922846208/CTHkwdBUAAE-k6r.jpg")        
        
    @commands.command()
    async def facepaw(self):
        """When the fail is meow enough."""
        await self.bot.say("https://66.media.tumblr.com/e32e3b520e81c2cb8d3d88e754991327/tumblr_inline_obd8kq9Bse1t8eu9z_500.gif")
    
    @commands.command()
    async def animesucks(self):
        """Use this before it enters 'Murica."""
        await self.bot.say("http://i1.kym-cdn.com/photos/images/newsfeed/000/708/423/caf.jpg")
        
    @commands.command()
    async def fuckanime(self):
        """Use this after it enters 'Murica."""
        await self.bot.say("http://www.meh.ro/original/2009_11/meh.ro2857.jpg")

    @commands.command()
    async def nukejapan(self):
        """You must do that. Clownpiece is an abomination."""
        await self.bot.say("https://discordcdn.com/attachments/196051622055378953/210631730208571395/IMG_0631.JPG")

    @commands.command()
    async def pizza(self):
        """Oh boy I'm so hungry."""
        await self.bot.say("http://www.tonysfoodphotos.com/data/photos/67_1stuffed_crust_pizza.jpg")
        
    @commands.command()
    async def piracy(self):
        """Unskippable comments in your bought website."""
        await self.bot.say("http://farm5.static.flickr.com/4032/4369403959_fe90464b27_o.jpg")
  
    @commands.command()
    async def disappointed(self):
        """I am disappoint."""
        await self.bot.say("https://media.giphy.com/media/3oAt21Fnr4i54uK8vK/giphy.gif")      
        
    @commands.command()
    async def mandms(self):
        """Lambdadelta likes M&Ms."""
        await self.bot.say("http://1.bp.blogspot.com/-rtC_BMawGH0/Tu6wXOwbZjI/AAAAAAAANCY/hmLDW8aOINc/s1600/6533753255_537c347d96_o.jpg")

    @commands.command()
    async def gowrong(self):
        """What could possibly go wrong?"""
        await self.bot.say("http://i.imgur.com/o1DnKkL.png")
        
    @commands.command()
    async def traitor(self):
        """You Resistance scum!"""
        await self.bot.say("http://i3.kym-cdn.com/photos/images/newsfeed/001/058/805/2ba.jpg")
        
    @commands.command()
    async def yeaaaah(self):
        """Let's do bizzare things!"""
        await self.bot.say("http://i0.kym-cdn.com/photos/images/newsfeed/000/829/841/5e0.gif")

    @commands.command()
    async def boo(self):
        """ULTRA SCARY."""
        await self.bot.say("http://i.imgur.com/4HbsKX1.gif")
        
    @commands.command()
    async def boobs(self):
        """They're actually called 'breasts', by the way."""
        await self.bot.say("http://imgur.com/download/zLYPDNR")

    @commands.command()
    async def panic(self):
        """What do I do?"""
        await self.bot.say("https://66.media.tumblr.com/67a97b5fdc620787d6bf194acdce77f5/tumblr_myxbzcPXGX1qlaxh8o1_400.gif")
        
    @commands.command()
    async def nofucks(self):
        """Instead of asking doctor who, I present you with a toad."""
        await self.bot.say("http://66.media.tumblr.com/8cd342cd9f94126ac6bd79f5bb3af7b4/tumblr_mqm5bwyHQR1qlaxh8o1_400.gif")  
        
    @commands.command()
    async def doge(self):
        """Awww......"""
        await self.bot.say("http://barkpost-assets.s3.amazonaws.com/wp-content/uploads/2013/11/dogesmall.jpg")

    @commands.command()
    async def limewire(self):
        """Do what you want cause a pirate is free."""
        await self.bot.say("http://i.imgur.com/1h6HMiV.gifv")
        
    @commands.command()
    async def praisethesun(self):
        """Praise it."""
        await self.bot.say("http://i.imgur.com/YA2WFS8.png")
        
    @commands.command()
    async def sun(self):
        """We all love her."""
        await self.bot.say("http://solarsystemexplore.com/wp-content/uploads/2012/11/The-Sun.jpg")

    @commands.command()
    async def meteorstrike(self):
        """Presented by Sabin and Tom Slattery."""
        await self.bot.say("http://static.fjcdn.com/gifs/What_a9d5b5_5443845.gif")
        
    @commands.command()
    async def suplex(self):
        """Presented by SABIN and TED WOOLSEY."""
        await self.bot.say("http://www.gamingrebellion.com/wp-content/uploads/2015/09/FF6-Train-Suplex.gif?9d7bd4")

    @commands.command()
    async def genesisdoes(self):
        """What Nintendon't."""
        await self.bot.say("http://static1.squarespace.com/static/550b8a2ae4b0558c356e47f5/t/55de6fa3e4b0b8c9e8eb629c/1440640932037/")

    @commands.command()
    async def nuke(self):
        """Wipe out everything."""
        await self.bot.say("http://www.chrisewings.com/images/Misc/images/Nuke%203_jpg.jpg")
        
    @commands.command()
    async def doesnotcompute(self):
        """DIVISION BY ZERO ERROR"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/193922029559349259/Does_Not_Compute.gif")
        
    @commands.command()
    async def drm(self):
        """The pirates are badass, too."""
        await self.bot.say("http://static.fjcdn.com/gifs/Drm+sucks+drm+is+not+good+for+anyone_2de156_4485223.gif")

    @commands.command()
    async def gooddaysir(self):
        """Presented by Willy Wonka."""
        await self.bot.say("http://giphy.com/gifs/reaction-angry-gFjbkip9OIIuI")

    @commands.command()
    async def fetish(self):
        """That is my fetish."""
        await self.bot.say("http://imgur.com/LiRYZeY")
        
    @commands.command()
    async def killthoseponies(self):
        """Bring them back to death."""
        await self.bot.say("http://www.dailyfreegames.com/images/thumbsfree/KTPON150.jpg")     

    @commands.command()
    async def itsover9000(self):
        """What does the scouter say about their power level?"""
        await self.bot.say("http://blog.sheasilverman.com/wp-content/uploads/2014/05/tumblr_lwhv2roIab1qd47jqo1_500.gif")    
        
    @commands.command()
    async def awake(self):
        """I have a bad feeling about this."""
        await self.bot.say("http://i.imgur.com/RqgiDtI.gif")
        
    @commands.command()
    async def weebstick(self):
        """Because we REALLY NEEDED an Overwatch GIF."""
        await self.bot.say("http://imgur.com/PIpsc02")

    @commands.command()
    async def notprepared(self):
        """You are dead."""
        await self.bot.say("http://i.imgur.com/Ch9TMSd.gif")

    @commands.command()
    async def dank(self):
        """Uhh."""
        await self.bot.say("http://i.imgur.com/EUChYKI.gifv")
        
    @commands.command()
    async def finalcountdown(self):
        """Venus isn't a good place to live."""
        await self.bot.say("http://b.vimeocdn.com/ts/234/533/234533071_640.jpg")

    @commands.command()
    async def pcmr(self):
        """Glorious PC Master Race."""
        await self.bot.say("https://i.ytimg.com/vi/jrxXyTHPPCw/hqdefault.jpg")

    @commands.command()
    async def ora(self):
        """Ora Ora Ora Ora!!!"""
        await self.bot.say("http://i.imgur.com/A2ZzU39.gif")

    @commands.command()
    async def ata(self):
        """ATATATATATATATA- *sigh* I'm tired."""
        await self.bot.say("http://i.imgur.com/UC5EUda.gif")

    @commands.command()
    async def frustrated(self):
        """I hate my life."""
        await self.bot.say("http://i.imgur.com/shlFpZM.gif")

    @commands.command()
    async def bendgate(self):
        """Yes, iPhone 6+s are still bent to this day."""
        await self.bot.say("http://pbs.twimg.com/media/By90YiIIcAAeyYh.jpg")

    @commands.command()
    async def getgood(self):
        """...it means get good."""
        await self.bot.say("http://i.imgur.com/XKw7Yot.gif")

    @commands.command()
    async def bye(self):
        """Goodbye!"""
        await self.bot.say("http://i.imgur.com/YXhYUud.gif")

    @commands.command()
    async def nom(self):
        """Eats-a-Otter"""
        await self.bot.say("http://imgur.com/zMJ0ErL")
        
    @commands.command()
    async def clap(self):
        """And it's Snow White clapping! Or maybe not."""
        clap = ["http://cdn2.business2community.com/wp-content/uploads/2014/02/SnowWhiteClapping8.gif", "https://cdn.discordapp.com/attachments/173967012123377664/193897102990901249/manicclap1.gif"]
        await self.bot.say(randchoice(clap))

    @commands.command()
    async def endlesseight(self):
        """15532"""
        await self.bot.say("http://2.bp.blogspot.com/_uj_QeQVH3-g/TByp6OOnSRI/AAAAAAAAAX8/0PS_lfCcto4/s1600/Suzumiya+Haruhi+endless+eight!.jpg")

    @commands.command()
    async def megaman(self):
        """A NEW MEGAMAN GAME!!"""
        await self.bot.say("http://i.imgur.com/I5tpeYT.gif")

    @commands.command()
    async def justinbieber(self):
        """[Insert Bieber song here]"""
        await self.bot.say("http://i3.kym-cdn.com/photos/images/newsfeed/000/628/701/e5f.gif")

    @commands.command()
    async def internet(self):
        """The internet? I thought it was a dinosaur?"""
        await self.bot.say("https://cdn.discordapp.com/attachments/174932651201921024/180800690233409537/10172634_10152398016887929_353810091488771162_n.jpg")

    @commands.command()
    async def zerofucks(self):
        """I don't care enough."""
        await self.bot.say("https://images-2.discordapp.net/.eJwVyEkOwyAMAMC_8ADMErHkN4hQg5TUCLuHqurf21zmMB_1WqfaVReZvAMcgyutQ7PQKtg0EuHZyhysK11QRErtV3sKg40x5exMssZZG30Od2Xjk9tM-OtTDIBj9rfG8VDfH8FeIes.-986DO-paeh4B02b83dM92oEf14.gif")

    @commands.command()
    async def leak(self):
        """Where's that dripping coming from?"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/199621074613305355/Leek.JPG")

    @commands.command()
    async def youdidnttry(self):
        """Loser."""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/200992165848023040/achievement-xbox.png")

    @commands.command()
    async def pingas(self):
        """SnooPING AS usual, I see?"""
        await self.bot.say("http://i1.kym-cdn.com/entries/icons/original/000/000/209/icon.png")

    @commands.command()
    async def burneverything(self):
        """We don't need no water."""
        clap = ["http://66.media.tumblr.com/b995f1503b36ae77f89a7bc103518f41/tumblr_o8vgzbMOdp1u591fzo1_400.gif",
            "http://static2.fjcdn.com/thumbnails/comments/Makes+you+just+want+to+burn+everything+_2914a81e5cbc5d99efb17fac58d18cc7.gif",
            "http://sd.keepcalm-o-matic.co.uk/i/keep-calm-and-burn-everything-2.png"]
        await self.bot.say(randchoice(clap))

    @commands.command()
    async def seraphna(self):
        """Everyone's 'favourite' moderator."""
        await self.bot.say("http://i.imgur.com/eTL6A4k.png")

    @commands.command()
    async def thatsthejoke(self):
        """Now laugh."""
        await self.bot.say("https://i.imgur.com/utzTCyo.png")

    @commands.command()
    async def kek(self):
        """Just don't kek yourself."""
        kek = ["https://cdn.discordapp.com/attachments/173967012123377664/202081415901216768/798.png",
               "http://i1.kym-cdn.com/photos/images/facebook/000/803/712/140.jpg"]
        return await self.bot.say(randchoice(kek))

    @commands.command()
    async def steam(self):
        """Turn the valve."""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/202092452574789633/did-you-mean-eccd6a67e1ca235245b50a61fd879a97.png")

    @commands.command()
    async def hankey(self):
        """If you eat fibre on Christmas Eve, he might come to your town!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/202183615164055552/unknown.png")
        
    @commands.command()
    async def opinion(self):
        """Your opinion isn't good."""
        await self.bot.say("https://cdn.discordapp.com/attachments/205815814316752897/211667870927683584/your_opinions_are_shit.jpeg")
        
    @commands.command()
    async def meiou(self):
        """Hades Attack!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/211696199760084992/hadesattack_2.gif") 

    @commands.command()
    async def alive(self):
        """Yep, I'm sure, I can feel a pulse."""
        await self.bot.say("https://cdn.discordapp.com/attachments/172006506525360129/203214935105339394/pfq7ers3oaowg3o1ik9f.jpg")

    @commands.command()
    async def donewithshit(self):
        """Yeah… no."""
        donewithshit = ["https://cdn.discordapp.com/attachments/173965999744221185/203516719203876864/funny_mew.png",
               "http://66.media.tumblr.com/db53616551186e6667ed91d70dd930e2/tumblr_naiu91b2r01r2g7mto5_r1_1280.png",
               "http://pre01.deviantart.net/baed/th/pre/f/2015/364/e/5/just_by_goshaag-d9m0idf.png",
               "http://66.media.tumblr.com/180d11323e589413cef030c93b2f9987/tumblr_myrlcqqNox1qe0snzo1_250.gif",
               "http://orig03.deviantart.net/9633/f/2014/246/3/3/dddd_by_combotron_robot-d7xvq1x.png"]
        return await self.bot.say(randchoice(donewithshit))
        
    @commands.command()
    async def feelthesalamon(self):
        """Feel it! I command you!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/203521186863382529/unknown.png")

    @commands.command()
    async def princessinanothercastle(self):
        """Toad does trolling."""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/203787385270435841/unknown.png")

    @commands.command()
    async def onlywaytobesure(self):
        """Nuke it from orbit?"""
        await self.bot.say("http://stream1.gifsoup.com/view/1010903/iron-man-jericho-o.gif")

    @commands.command()
    async def kitty(self):
        """Dare you poke the kitty?"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/204725484414697472/Z.png")

    @commands.command()
    async def spittake(self):
        """Dare you poke the kitty?"""
        await self.bot.say("http://media2.popsugar-assets.com/files/thumbor/kFAELJd35-6yF4-oVDc6tM3UnNM/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2014/07/02/996/n/1922283/d01950272ef3ac9e_83551143/i/When-Kramer-Does-Epic-Spit-Take.gif")

    @commands.command()
    async def latetotheparty(self):
        """And everyone's gone home."""
        await self.bot.say("http://i3.kym-cdn.com/photos/images/original/000/990/241/902.gif")

    @commands.command()
    async def nerds(self):
        """No, not the band…"""
        await self.bot.say("http://i.imgur.com/680s09d.gif")

    @commands.command()
    async def cackle(self):
        """I revel in your misfortune."""
        cackle = ["http://i.imgur.com/82e7eOE.gif","http://i.imgur.com/fWqFxOL.gif","http://i.imgur.com/4qw3RoV.gif"]
        return await self.bot.say(randchoice(cackle))
        
    @commands.command()
    async def damnit(self):
        """Damn it all to hell!"""
        await self.bot.say("http://i.imgur.com/eELH7YV.gif")

    @commands.command()
    async def splatoon(self):
        """Are you a kid or a squid?"""
        await self.bot.say("http://33.media.tumblr.com/7975df6e6d51a0d30d4d82f18f9e12f2/tumblr_nm4mbvkxDL1ra1vfao1_400.gif")

    @commands.command()
    async def timtams(self):
        """We shall set up an exchange programme."""
        await self.bot.say("http://pre01.deviantart.net/8b15/th/pre/i/2014/312/1/b/freedom_planet_tim_tam_candy_bar_by_novashenron-d85rdvr.jpg")

    @commands.command()
    async def getthedj(self):
        """Cocaine habit optional."""
        await self.bot.say("https://i427.photobucket.com/albums/pp352/GothDraagun/Pokemon/exploud.gif")

    @commands.command()
    async def shitpost(self):
        """Only the finest quality!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/110373943822540800/192833561873743874/shit.gif")

    @commands.command()
    async def stahp(self):
        """Stahp it Penders!"""
        stahp = ["http://weknowmemes.com/generator/uploads/generated/g1379092610384759364.jpg",
                "http://s2.quickmeme.com/img/54/54b4ef9552fc06ca35b9297534b3ad8df2bccbf8b9da8d09c7d014f26947b788.jpg",
                "https://cdn.meme.am/instances/400x/55275802.jpg",
                "https://cdn.meme.am/instances/35884590.jpg",
                "http://s.quickmeme.com/img/78/7835258a77bff1ef34a7e9220c05c46c2297ae2548c5f90aac0c41facb534639.jpg"]
        return await self.bot.say(randchoice(stahp))
        
    @commands.command()
    async def justright(self):
        """In the Goldilocks zone"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/225688671943262218/when_you_dragon_boost_just_right_by_wyviryn-da47yb2.png")

    @commands.command()
    async def juststrife(self):
        """In the Strifilocks zone"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/225682792497938432/just_strife.png")

    @commands.command()
    async def twinsatcannon(self):
        """When you want something done right, overdo it"""
        await self.bot.say("https://cdn.discordapp.com/attachments/205815814316752897/225717296209985536/TwinSatelliteCannon2.gif")

    @commands.command()
    async def offensive(self):
        """When you want something done right, overdo it"""
        await self.bot.say("https://cdn.discordapp.com/attachments/205815814316752897/225975861772288000/YOUR_POST_IS_TOO_OFFENSIVE.jpg")

    @commands.command()
    async def winner(self):
        """Your worth it!"""
        winner = ["https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "https://cdn.discordapp.com/attachments/173967012123377664/226089036706611200/latest.png",
                "http://d.ibtimes.co.uk/en/full/337429/michael-winner.jpg"]
        return await self.bot.say(randchoice(winner))
        
    @commands.command()
    async def loser(self):
        """I'm a loser baby, so why don't you kill me?"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/226095352338579467/037.png")

    @commands.command()
    async def butthurt(self):
        """Do you want a cushion to sit on?"""
        await self.bot.say("https://cdn.discordapp.com/attachments/205815814316752897/226095936370114561/7600a831b4089d435e6410a8199f1f2e.png")

    @commands.command()
    async def misdirection(self):
        """The face of being struck by a deadly attack."""
        await self.bot.say("https://cdn.discordapp.com/attachments/196051622055378953/226802142143447040/IMG_1087.PNG")
        
    @commands.command()
    async def noot(self):
        """Noot noot EXTREME!"""
        await self.bot.say("http://i0.kym-cdn.com/photos/images/original/001/170/325/910.gif")
        
    @commands.command()
    async def cockblocked(self):
        """Blocking Crocks"""
        await self.bot.say("https://cdn.discordapp.com/attachments/172098189388808193/229014327208837120/Crock_Blocked.jpg")
        
    @commands.command()
    async def moonrunes(self):
        """Konnichi wa! Did you understand this?"""
        await self.bot.say("http://orig13.deviantart.net/313e/f/2014/212/2/d/moonspeak_by_paulgq-d7t5kur.png")
        
    @commands.command()
    async def sweet(self):
        """Really sweet!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/205815814316752897/228612028451913729/2Q.png")
        
    @commands.command()
    async def power(self):
        """POWERRRRRRRRRRRR SPEED"""
        await self.bot.say("https://cdn.discordapp.com/attachments/205815814316752897/228611354632650752/2Q.png")
        
    @commands.command()
    async def pikachu(self):
        """PIKACHUUUUUUUUUUUUUUUUUUUUU"""
        pikachu = ["https://cdn.discordapp.com/attachments/172098189388808193/227975719546781696/lmao_2.gif",
                   "http://i3.kym-cdn.com/photos/images/newsfeed/001/172/937/130.gif"]
        await self.bot.say(randchoice(pikachu))
        
    @commands.command()
    async def sonicmania(self):
        """Mania?"""
        smania = ["http://pre13.deviantart.net/77af/th/pre/f/2016/220/a/4/sonimani_poro_by_poroisasaki-dad3k2x.png",
                   "https://www.youtube.com/watch?v=xtqgkPCEIP8"]
        await self.bot.say(randchoice(smania))
        
    @commands.command()
    async def sleep(self):
        """Are you really tired?"""
        await self.bot.say("https://s-media-cache-ak0.pinimg.com/236x/2e/2d/00/2e2d006790ff573e1e5cab5c14ce74bb.jpg")
        
    @commands.command()
    async def cringefest(self):
        """Not safe for your sanity!"""
        cringe = ["https://cdn.discordapp.com/attachments/173966944351944704/227638265719685121/There_it_exists_now.png",
                  "Sticker Star is better than Super Paper Mario anyways."]
        await self.bot.say(randchoice(cringe))

    @commands.command()
    async def megaman(self):
        """Why is he a blue 'bomber'?"""
        await self.bot.say("http://fc02.deviantart.net/fs71/f/2014/098/f/4/ssb_mega_man_final_smash_gif_by_kiradaidohji-d7dpvau.gif")
        
    @commands.command()
    async def tallgeese(self):
        """The cure for..."""
        await self.bot.say("https://cdn.discordapp.com/attachments/205815814316752897/227631619429761024/tallgeese.gif")
        
    @commands.command()
    async def trumpcard(self):
        """I'll activate my trump card!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/171613498025967616/227302745135251456/DonaldTrump1.png")
        
    @commands.command()
    async def pls(self):
        """Please!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/196051622055378953/231141348302913537/13442152_251494178558832_2830693608439609956_n.jpg")
        
    @commands.command()
    async def spellchecker(self):
        """Better use it before you get shot!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/173967012123377664/227181413127028737/1audmk.jpg")
        
    @commands.command()
    async def ace(self):
        """...of diamonds!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/205815814316752897/230804809723281409/Ace_of_Spade.png")

    @commands.command()
    async def nfkrz(self):
        """Some dude"""
        nfkrz = ["http://i0.kym-cdn.com/entries/icons/original/000/020/771/nfkrz.jpg",
                 "https://ih0.redbubble.net/image.218911146.3367/drawstring_bag,x1404-bg,f8f8f8.u1.jpg",
                 "https://img.ifcdn.com/images/8dd7409a1446ed08a5db3ea4c974451b4cd5deae3a8fc8e171ab88253d9708c4_1.jpg",
                 "https://img.ifcdn.com/images/74667adf5461f6ffd345efb63299fc945319463421016cf4207474edb496d5dc_1.jpg",
                 "https://i.ytimg.com/vi/w8hnS3VE-Ds/maxresdefault.jpg",
                 "http://i1.kym-cdn.com/photos/images/facebook/001/141/529/a61.png",
                 "https://cdn.discordapp.com/attachments/225788942916517890/231204539578056704/nfkrz_star.png"
                ]
        await self.bot.say(randchoice(nfkrz))

    @commands.command()
    async def flynn(self):
        """Cool under pressure"""
        flynn = ["http://i.imgur.com/fo9qF4t.gif"]
        await self.bot.say(randchoice(flynn))

    @commands.command()
    async def understatement(self):
        """Because there just aren't enough memes yet, apparently"""
        understatement = ["https://cdn.discordapp.com/attachments/205815814316752897/229716017826365441/ididanotherthing.png"]
        await self.bot.say(randchoice(understatement))

def setup(bot):
    bot.add_cog(randimages(bot))

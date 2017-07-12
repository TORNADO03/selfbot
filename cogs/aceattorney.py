import discord
from discord.ext import commands

'''My Ace Attorney commands'''


class AceAttorney:

    def __init__(self, bot):
        self.bot = bot

    async def simple_embed(self, text, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = text
        await self.bot.say("", embed=embed)
		
    @commands.command(pass_context=True)
    async def holy(self, ctx):
        """Edgeworth's Response (image)"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="https://i.imgur.com/KBWpDpW.png"))
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="https://i.imgur.com/BixOUBV.png"))
        
    @commands.command(pass_context=True)
    async def holytext(self, ctx):
        """Edgeworth's Response (text)"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Miles Edgeworth", color=discord.Color.blue())
        embed.description = "This one single statement is so full of contradictions... For a moment there, I thought I was going to collapse."
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def press(self, ctx):
        """HOLD IT!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/umt4Pr2.png"))
        
    @commands.command(pass_context=True)
    async def object(self, ctx):
        """OBJECTION!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/0GTlFg0.png"))
        
    @commands.command(pass_context=True)
    async def take(self, ctx):
        """TAKE THAT!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/qPIwEaq.png"))
        
    @commands.command(pass_context=True)
    async def silence(self, ctx):
        """SHUT THE FUCK UP!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/nOZoypt.png"))
        
    @commands.command(pass_context=True)
    async def gotcha(self, ctx):
        """GOTCHA!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/29ZvDWm.png"))
        
    @commands.command(pass_context=True)
    async def enough(self, ctx):
        """ENOUGH!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/paNw1dh.png"))
        
    @commands.command(pass_context=True)
    async def fast(self, ctx):
        """NOT SO FAST!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/Nab2PLO.png"))
        
    @commands.command(pass_context=True)
    async def got(self, ctx):
        """GOT IT!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/J3X6Fbd.png"))
        
    @commands.command(pass_context=True)
    async def eureka(self, ctx):
        """EUREKA!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/O8gVn3q.png"))
	
    @commands.command(pass_context=True)
    async def overruled(self, ctx):
        """OVERRULED!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/LWA0zBP.png"))
	
    @commands.command(pass_context=True)
    async def hangon(self, ctx):
        """HANG ON!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/ROuT68M.png"))
	
    @commands.command(pass_context=True)
    async def havealook(self, ctx):
        """HAVE A LOOK!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/heFKpaV.png"))
	
    @commands.command(pass_context=True)
    async def satorha(self, ctx):
        """SATORHA!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/l81174m.png"))
	
    @commands.command(pass_context=True)
    async def insolence(self, ctx):
        """SUCH INSOLENCE!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/d9Pdd9D.png"))
	
    @commands.command(pass_context=True)
    async def welcome(self, ctx):
        """WELCOME!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/sLmPuWl.png"))
	
    @commands.command(pass_context=True)
    async def objectright(self, ctx):
        """ObjectRight"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/V5drICD.png"))

def setup(bot):
    bot.add_cog(AceAttorney(bot))

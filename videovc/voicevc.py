from redbot.core import commands

class VoiceVC(commands.Cog):
    """My custom cog"""

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def vc(self, ctx):
        """Generate a video chat url"""
        try:
            await ctx.send("Here's your link: https://discordapp.com/channels/" + str(ctx.guild.id) + "/" + str(ctx.author.voice.channel.id))
        except:
            return await self._embed_msg(
                ctx,
                title=_("Unable To Generate Link"),
                description=_("Connect to a voice channel first."),
            )
import discord.embeds as e
from discord.abc import Messageable
from discord.ext.commands import Context
from discord.colour import Colour

HORNET_COLOUR = Colour(0x79414B)

class EmbedContext():
    def __init__(self, context: Context):
        self.context = context

    async def embedMessage(self, message=None, title=None, fields=None):
        construct = e.Embed(description=message, title=title, colour=HORNET_COLOUR)
        if fields:
            for f in fields:
                inline = f[2] if len(f) == 3 else True
                construct.add_field(name=f[0], value=f[1], inline=inline)
        await self.context.send(embed=construct)

    async def embedReply(self, message=None, title=None, fields=None):
        construct = e.Embed(description=message, title=title, colour=HORNET_COLOUR)
        if fields:
            for f in fields:
                inline = f[2] if len(f) == 3 else True
                construct.add_field(name=f[0], value=f[1], inline=inline)
        await self.context.reply(embed=construct, mention_author=False)

async def embedReply(context : Context, message=None, title=None, fields=None):
    construct = e.Embed(description=message, title=title, colour=HORNET_COLOUR)
    if fields:
        for f in fields:
            inline = f[2] if len(f) == 3 else False
            construct.add_field(name=f[0], value=f[1], inline=inline)
    await context.reply(embed=construct, mention_author=False)

async def embedMessage(dest: Messageable, message=None, title=None, fields=None):
    """Send an embed message to the destination channel/context, with optional fields as a List[Tuple[str, str]]"""
    construct = e.Embed(description=message, title=title, colour=HORNET_COLOUR)
    if fields:
        for f in fields:
            inline = f[2] if len(f) == 3 else True
            construct.add_field(name=f[0], value=f[1], inline=inline)
    await dest.send(embed=construct)
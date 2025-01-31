from typing import Union
import discord
from discord import Emoji, PartialEmoji
from discord.ext.commands import EmojiConverter, EmojiNotFound, Context, Bot
import discord.ext.commands.converter
import emoji

bot : Bot = None  # set up in Hornet.py

async def toEmoji(ctx : Context, reference: str) -> Union[str, Emoji]:
    """ID/emoji string to either Emoji or str if unicode emoji"""
    try:
        return await EmojiConverter().convert(ctx, reference)
    except EmojiNotFound as e:
        if is_emoji(reference): return reference # catch unicode emoji
        else: raise e

def toString(emoji: Union[Emoji, str]) -> str:
    """Emoji client embed or unicode string"""
    if isinstance(emoji, str): return emoji
    if isinstance(emoji, PartialEmoji):
        if emoji.id is None: return emoji.name
    return f"<:{emoji.name}:{emoji.id}>"

def is_emoji(codepoint : str):
    if 0x1F1E6 <= ord(codepoint) <= 0x1F1FF: return True
    return emoji.is_emoji(codepoint)
import datetime
import discord


def str_to_datetime(s: str):
    return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f")


def embed_to_dict(embed: discord.Embed):
    pass  # TODO add embed support


def attachment_to_dict(attachment: discord.Attachment):
    pass  # TODO add attachment support

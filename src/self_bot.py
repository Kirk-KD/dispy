import discord

from src import event
from src.json_read_write import JSONReadWrite


class SelfBot(discord.Client):
    def __init__(self, save_dir: str, *args, **kwargs):
        self.json = JSONReadWrite(save_dir)
        self.user_watchlist = [711712742310019073, 814166461228515329]

        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print("SELF BOT READY: {}".format(self.user))

    async def on_message(self, message):
        if message.author.id in self.user_watchlist:
            e = event.DMMessageRecieved(message)
            self.json.add_event(e)

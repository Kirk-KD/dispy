import datetime
import discord

event_type = [
    "DM Message Received"
]


class Event:
    def __init__(self, event_type: int, timestamp: datetime.datetime):
        self.event_type = event_type
        self.timestamp = timestamp
    
    def make_json(self, data: dict={}):
        return {
            "event_type": event_type[self.event_type],
            "timestamp": str(self.timestamp),
            "data": data
        }

    def json(self):
        return self.make_json()

    def make_str(self, info: str=None):
        return "{}@{}{}".format(
            event_type[self.event_type], self.timestamp, (":\n\t" + info) if info is not None else ""
        )
    
    def __str__(self):
        return self.make_str()


class DMMessageRecieved(Event):
    def __init__(self, message: discord.Message):
        super().__init__(0, message.created_at)
        self.message = message
    
    def json(self):
        return self.make_json({
            "message_id": self.message.id,
            "content": self.message.content,
            "user_id": self.message.author.id,
            "embeds": [],  # TODO add embed support
            "attachments": []  # TODO add attachment support
        })
    
    def __str__(self):
        return self.make_str(self.message.content)


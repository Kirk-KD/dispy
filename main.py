from src import self_bot
from dotenv import load_dotenv
import os

load_dotenv()

bot = self_bot.SelfBot("data.json")
bot.run(os.getenv("TOKEN"))  # put token in .env for now for testing purposes

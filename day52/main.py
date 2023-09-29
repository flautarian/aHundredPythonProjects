
import os
from InstaFollower import InstaFollower

CHROME_DRIVER_PATH = os.environ["DRIVER_PATH"]
SIMILAR_ACCOUNT = os.environ["INS_SIMILAR_ACCOUNT"]
USERNAME = os.environ["INS_USERNAME"]
PASSWORD = os.environ["INS_PASSWORD"]

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

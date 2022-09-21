import guilded
from guilded.ext import commands

import json
import logging
import os
from dotenv import load_dotenv
from time import time


VERSION = "4.0.2"


# Logging
logging.basicConfig(
    level=logging.INFO,
    filename=f"logs/{time()}.log",
    filemode="w",
    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
)

logging.warning("warning")
logging.error("error")
logging.critical("critical")

# Load dotenv file
load_dotenv("keys.env")
TOKEN = os.getenv("GUILDED")

# Load config file
with open("config.json", "r") as f:
    config = json.load(f)

# Load status file
with open("statuses.json", "r") as f:
    statusjson = json.load(f)


# Grab statuses from statuses.json
statuses = statusjson["statuses"]

# Grab vars from config.json
DEFAULT_PREFIX = config["DEFAULT_PREFIX"]
OWNER_IDS = config["OWNER_IDS"]

bot = commands.Bot(
    command_prefix=DEFAULT_PREFIX,
    owner_ids=OWNER_IDS
)

bot.version = VERSION
bot.ready = False

@bot.event
async def on_ready():
    if not bot.ready:
        print(f"logged in as {bot.user}")
        guild_count = 0
        for guild in bot.guilds:
            print(f"- {guild.id} (name: {guild.name})")
            guild_count = guild_count + 1

        print(f"{bot.user} is in {guild_count} guild(s)")

        bot.ready = True


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send('pong!')

bot.run(TOKEN)
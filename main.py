"""
==========================================================
ONICORE BOTS

Bot Name  : Jhaplupirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

Main Entry Point
Production Ready
Fully Commented

==========================================================
"""

# ==========================================================
# Required Imports
# ==========================================================

from pyrogram import Client, idle
from pyrogram.enums import ParseMode

import config

from core.logger import (
    LOGGER,
    success,
    error
)

from core.startup import startup

# ==========================================================
# Create Bot Client
# ==========================================================
#
# This is the main bot client.
# Every handler will be attached to this.
#
# ==========================================================

app = Client(

    name="Jhaplupirobot",

    api_id=config.API_ID,

    api_hash=config.API_HASH,

    bot_token=config.BOT_TOKEN,

    parse_mode=ParseMode.HTML

)

# ==========================================================
# Bot Started Event
# ==========================================================

@app.on_start()
async def bot_started(client):
    """
    Runs automatically after the bot starts.
    """

    await startup.initialize(client)

# ==========================================================
# Main Function
# ==========================================================

async def main():

    """
    Starts the bot.

    Loads all plugins.

    Executes startup tasks.

    Keeps bot alive.
    """

    success("Starting Telegram Client...")

    await app.start()

    success("Bot Started Successfully.")

    await idle()

    success("Stopping Bot...")

    await app.stop()

    success("Bot Stopped Successfully.")

# ==========================================================
# Run Program
# ==========================================================

if __name__ == "__main__":

    try:

        app.run(main())

    except KeyboardInterrupt:

        LOGGER.info("Bot Interrupted.")

    except Exception as e:

        error(str(e))

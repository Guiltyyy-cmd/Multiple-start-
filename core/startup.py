"""
==========================================================
ONICORE BOTS

Bot Name  : Jhaplupirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

Startup Manager
Production Ready
Fully Commented

==========================================================
"""

# ==========================================================
# Required Imports
# ==========================================================

from pyrogram import Client
from pyrogram.errors import RPCError

import config

from database.mongo import db
from core.logger import (
    success,
    warning,
    error,
    startup_banner
)

# ==========================================================
# Startup Manager Class
# ==========================================================

class StartupManager:
    """
    Handles every startup task of the bot.

    Functions:
    • MongoDB Connection Check
    • Telegram Login Check
    • Owner Restart Notification
    • Startup Logs
    """

    def __init__(self):

        self.me = None

    # ======================================================
    # Check MongoDB
    # ======================================================

    async def check_database(self):

        connected = await db.ping()

        if connected:
            success("MongoDB Connected Successfully.")
            return True

        error("Unable to connect MongoDB.")

        return False

    # ======================================================
    # Get Bot Information
    # ======================================================

    async def get_bot_info(self, app: Client):

        self.me = await app.get_me()

        success(
            f"Logged in as @{self.me.username}"
        )

        return self.me

    # ======================================================
    # Notify Owner
    # ======================================================

    async def notify_owner(self, app: Client):

        """
        Sends restart message
        only to OWNER_ID.
        """

        try:

            await app.send_message(

                chat_id=config.OWNER_ID,

                text=config.RESTART_MESSAGE.format(

                    BOT_BRAND=config.BOT_BRAND,

                    DEV_USERNAME=config.DEV_USERNAME,

                    MARKETING=config.MARKETING

                )

            )

            success("Restart message sent.")

        except RPCError as e:

            warning(
                f"Owner Notification Failed : {e}"
            )

    # ======================================================
    # Complete Startup
    # ======================================================

    async def initialize(self, app: Client):

        """
        Executes every startup task.
        """

        startup_banner()

        success("Checking Database...")

        await self.check_database()

        success("Fetching Bot Information...")

        await self.get_bot_info(app)

        success("Sending Restart Notification...")

        await self.notify_owner(app)

        success("Startup Completed Successfully.")


# ==========================================================
# Global Startup Object
# ==========================================================

startup = StartupManager()

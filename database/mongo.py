"""
==========================================================
ONICORE BOTS

Bot Name  : Jhaplupirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

MongoDB Connection
Production Ready
Fully Commented

==========================================================
"""

# --------------------------------------------------------
# Import Required Libraries
# --------------------------------------------------------

from motor.motor_asyncio import AsyncIOMotorClient
import config


# --------------------------------------------------------
# MongoDB Class
#
# This class is responsible for:
#
# • Connecting MongoDB
# • Creating collections
# • Returning collection objects
#
# Every database operation in the bot
# will use this class.
# --------------------------------------------------------

class Database:

    def __init__(self):

        # --------------------------------------------
        # Create Mongo Client
        # --------------------------------------------

        self.client = AsyncIOMotorClient(config.MONGO_URI)

        # --------------------------------------------
        # Database Name
        #
        # Change only if required.
        # --------------------------------------------

        self.database = self.client["Jhaplupirobot"]

        # --------------------------------------------
        # Collections
        # --------------------------------------------

        self.users = self.database["users"]

        self.settings = self.database["settings"]

        self.files = self.database["files"]

        self.admins = self.database["admins"]

        self.banned = self.database["banned"]

        self.force_sub = self.database["force_sub"]

    # ====================================================
    # Check Mongo Connection
    # ====================================================

    async def ping(self):

        """
        Tests MongoDB connection.

        Returns:
            True  -> Connected
            False -> Failed
        """

        try:

            await self.client.admin.command("ping")

            return True

        except Exception as error:

            print(f"[MongoDB] Connection Failed : {error}")

            return False

    # ====================================================
    # User Collection
    # ====================================================

    async def add_user(self, user_id: int):

        """
        Add new user if not exists.
        """

        user = await self.users.find_one(
            {
                "_id": user_id
            }
        )

        if user:
            return False

        await self.users.insert_one(
            {
                "_id": user_id
            }
        )

        return True

    async def is_user_exist(self, user_id: int):

        """
        Check whether user exists.
        """

        user = await self.users.find_one(
            {
                "_id": user_id
            }
        )

        return bool(user)

    async def total_users(self):

        """
        Returns total registered users.
        """

        return await self.users.count_documents({})

    # ====================================================
    # Admin Collection
    # ====================================================

    async def total_admins(self):

        return await self.admins.count_documents({})

    # ====================================================
    # Ban Collection
    # ====================================================

    async def total_banned(self):

        return await self.banned.count_documents({})

    # ====================================================
    # File Collection
    # ====================================================

    async def total_files(self):

        return await self.files.count_documents({})

    # ====================================================
    # Force Subscribe Collection
    # ====================================================

    async def total_fsub(self):

        return await self.force_sub.count_documents({})


# --------------------------------------------------------
# Global Database Object
#
# Import this anywhere using:
#
# from database.mongo import db
#
# --------------------------------------------------------

db = Database()

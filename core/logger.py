"""
==========================================================
ONICORE BOTS

Bot Name  : Jhaplupirobot
Developer : @BlurpleOg
Marketing  : #onicore_bots

Professional Logger
Production Ready
Fully Commented

==========================================================
"""

# ==========================================================
# Import Required Libraries
# ==========================================================

import logging
import os
import sys

# ==========================================================
# Create Logs Folder Automatically
# ==========================================================

# If logs folder doesn't exist,
# it will be created automatically.

os.makedirs("logs", exist_ok=True)

# ==========================================================
# Log Format
# ==========================================================

LOG_FORMAT = (
    "[%(asctime)s] "
    "[%(levelname)s] "
    "%(name)s : %(message)s"
)

DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

# ==========================================================
# Main Logger Configuration
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT,
    handlers=[
        logging.FileHandler(
            "logs/bot.log",
            encoding="utf-8"
        ),
        logging.StreamHandler(sys.stdout)
    ]
)

# ==========================================================
# Main Logger Object
# ==========================================================

LOGGER = logging.getLogger("Jhaplupirobot")

# ==========================================================
# Startup Banner
# ==========================================================

def startup_banner():
    """
    Prints startup information in logs.
    """

    LOGGER.info("=" * 60)
    LOGGER.info("Jhaplupirobot Starting...")
    LOGGER.info("Developer : @BlurpleOg")
    LOGGER.info("Marketing : #onicore_bots")
    LOGGER.info("Production Mode Enabled")
    LOGGER.info("=" * 60)

# ==========================================================
# Success Logger
# ==========================================================

def success(message: str):
    """
    Log Success Message.
    """

    LOGGER.info(f"✅ {message}")

# ==========================================================
# Warning Logger
# ==========================================================

def warning(message: str):
    """
    Log Warning Message.
    """

    LOGGER.warning(f"⚠️ {message}")

# ==========================================================
# Error Logger
# ==========================================================

def error(message: str):
    """
    Log Error Message.
    """

    LOGGER.error(f"❌ {message}")

# ==========================================================
# Critical Logger
# ==========================================================

def critical(message: str):
    """
    Log Critical Error.
    """

    LOGGER.critical(f"🔥 {message}")

# ==========================================================
# Debug Logger
# ==========================================================

def debug(message: str):
    """
    Log Debug Message.
    """

    LOGGER.debug(message)

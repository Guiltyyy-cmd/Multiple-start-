"""
==========================================================
ONICORE BOTS

Bot Name  : Jhaplupirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

Random Picture Manager
Production Ready
Fully Commented

==========================================================
"""

# ==========================================================
# Required Imports
# ==========================================================

import random
import config

# ==========================================================
# Last Picture Cache
# ==========================================================
#
# Stores the last picture index.
# Prevents same image from appearing twice in a row.
#
# ==========================================================

_last_index = None


# ==========================================================
# Get Random Start Picture
# ==========================================================

def get_random_start_pic():
    """
    Returns a random picture.

    Same image will never repeat
    consecutively.

    Returns:
        str
    """

    global _last_index

    total = len(config.START_PICS)

    # If only one image exists,
    # return it directly.
    if total <= 1:
        return config.START_PICS[0]

    while True:

        index = random.randint(0, total - 1)

        if index != _last_index:

            _last_index = index

            return config.START_PICS[index]


# ==========================================================
# About Picture
# ==========================================================

def get_about_pic():
    """
    Returns About Picture.
    """

    return config.ABOUT_PIC


# ==========================================================
# Force Subscribe Picture
# ==========================================================

def get_fsub_pic():
    """
    Returns Force Subscribe Picture.
    """

    return config.FSUB_PIC


# ==========================================================
# Channels Picture
# ==========================================================

def get_channels_pic():
    """
    Returns Channels Picture.

    Currently using About Picture.

    Later you can add:

    CHANNELS_PIC

    inside config.py
    """

    return config.ABOUT_PIC

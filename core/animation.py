"""
==========================================================
ONICORE BOTS

Bot Name  : Jhaplupirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

Loading Animation
Production Ready
Fully Commented

==========================================================
"""

# ==========================================================
# Required Imports
# ==========================================================

import asyncio
import random

# ==========================================================
# Random Emojis
# ==========================================================

EMOJIS = [

    "🚀",
    "⚡",
    "💎",
    "✨",
    "🌈",
    "⭐",
    "🎯",
    "🔥",
    "💫"

]

# ==========================================================
# Progress Values
# ==========================================================

PROGRESS = [

    7,
    18,
    33,
    41,
    57,
    66,
    78,
    91,
    100

]

# ==========================================================
# Progress Bar Generator
# ==========================================================

def progress_bar(percent: int):

    """
    Returns unicode progress bar.

    Example:

    ■■■□□□□□□□
    """

    total = 10

    filled = round(percent / 10)

    empty = total - filled

    return "■" * filled + "□" * empty


# ==========================================================
# Loading Animation
# ==========================================================

async def play_animation(message):

    """
    Plays loading animation.

    After completion,

    Returns edited message.
    """

    emoji = random.choice(EMOJIS)

    for value in PROGRESS:

        await message.edit(

            f"""
<b>{emoji} 𝗝𝗵𝗮𝗽𝗹𝘂𝗣𝗶𝗿𝗼𝗯𝗼𝘁</b>

<blockquote>

<b>ʟᴏᴀᴅɪɴɢ...</b>

<code>{progress_bar(value)}</code>

<b>{value}%</b>

</blockquote>
"""

        )

        await asyncio.sleep(

            random.uniform(
                0.35,
                0.60
            )

        )

    return message


# ==========================================================
# Delete Animation
# ==========================================================

async def finish_animation(message):

    """
    Deletes animation message.
    """

    try:

        await message.delete()

    except:

        pass

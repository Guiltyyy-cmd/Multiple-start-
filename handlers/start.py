"""
==========================================================
ONICORE BOTS

Bot Name  : JhapluPirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

Start Handler

==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pyrogram import Client, filters
from pyrogram.types import Message

import config

from core.animation import (
    play_animation,
    finish_animation
)

from core.buttons import (
    start_buttons
)

from utils.random_pic import (
    get_random_start_pic
)

from utils.cooldown import (
    can_show_animation,
    update_animation_time
)

# ==========================================================
# Admin Check
# ==========================================================

def is_admin(user_id: int) -> bool:
    """
    Returns True
    if Owner/Admin.
    """

    return (
        user_id == config.OWNER_ID
        or user_id in config.ADMINS
    )


# ==========================================================
# HTML Mention
# ==========================================================

def html_mention(user):
    """
    Clickable user hyperlink.

    Opens profile when clicked.
    """

    return (
        f"<a href='tg://user?id={user.id}'>"
        f"{user.first_name}"
        f"</a>"
    )


# ==========================================================
# Start Command
# ==========================================================

@Client.on_message(
    filters.private &
    filters.command("start")
)
async def start_handler(
    client,
    message: Message
):

    # ----------------------------------------
    # Delete User Command
    # ----------------------------------------

    try:
        await message.delete()
    except:
        pass

    user = message.from_user

    mention = html_mention(user)

    admin = is_admin(user.id)

    # ----------------------------------------
    # Loading Animation
    # ----------------------------------------

    if can_show_animation(user.id):

        loading = await message.reply_text(
            "<b>Starting...</b>"
        )

        await play_animation(
            loading
        )

        await finish_animation(
            loading
        )

        update_animation_time(
            user.id
        )

    # ----------------------------------------
    # Random Picture
    # ----------------------------------------

    picture = get_random_start_pic()

    # ----------------------------------------
    # Caption
    # ----------------------------------------

    caption = config.START_MESSAGE.format(

        mention=mention,

        MARKETING=config.MARKETING

    )

    # ----------------------------------------
    # Send Start Photo
    # ----------------------------------------

    await message.reply_photo(

        photo=picture,

        caption=caption,

        reply_markup=start_buttons(admin)

  )

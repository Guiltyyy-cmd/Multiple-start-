"""
==========================================================
ONICORE BOTS

Bot Name  : JhapluPirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

callbacks.py

Handles every callback button.

==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InputMediaPhoto
)

import config

from core.buttons import (
    start_buttons,
    about_buttons,
    channels_buttons
)

from utils.random_pic import (
    get_random_start_pic,
    get_about_pic,
    get_channels_pic
)


# ==========================================================
# Callback Handler
# ==========================================================

@Client.on_callback_query()
async def callback_handler(
    client: Client,
    query: CallbackQuery
):

    """
    Main Callback Router
    """

    data = query.data

    user = query.from_user

    mention = (
        f"<a href='tg://user?id={user.id}'>"
        f"{user.first_name}"
        "</a>"
    )

    admin = (

        user.id == config.OWNER_ID

        or

        user.id in config.ADMINS

)
      # ==========================================================
    # CLOSE BUTTON
    # ==========================================================

    if data == "close":

        await query.answer()

        try:

            await query.message.delete()

        except Exception:

            pass

        return

    # ==========================================================
    # BACK TO START
    # ==========================================================

    if data == "back_start":

        picture = get_random_start_pic()

        caption = config.START_MESSAGE.format(

            mention=mention,

            MARKETING=config.MARKETING

        )

        await query.message.edit_media(

            media=InputMediaPhoto(

                media=picture,

                caption=caption

            ),

            reply_markup=start_buttons(admin)

        )

        await query.answer()

        return

    # ==========================================================
    # ABOUT PANEL
    # ==========================================================

    if data == "about":

        picture = get_about_pic()

        await query.message.edit_media(

            media=InputMediaPhoto(

                media=picture,

                caption=config.ABOUT_MESSAGE

            ),

            reply_markup=about_buttons(admin)

        )

        await query.answer()

        return

    # ==========================================================
    # CHANNELS PANEL
    # ==========================================================

    if data == "channels":

        picture = get_channels_pic()

        await query.message.edit_media(

            media=InputMediaPhoto(

                media=picture,

                caption=config.CHANNELS_MESSAGE

            ),

            reply_markup=channels_buttons(admin)

        )

        await query.answer()

        return
          # ==========================================================
    # SETTINGS PANEL
    # ==========================================================

    if data == "settings":

        # User Protection

        if not admin:

            await query.answer(

                "❌ You are not allowed to use this panel.",

                show_alert=True

            )

            return

        # Open Settings

        from core.buttons import settings_buttons

        text = f"""
<blockquote><b>⚙️ 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦 𝗣𝗔𝗡𝗘𝗟</b></blockquote>

<b>🤖 Bot :</b> {config.BOT_BRAND}
<b>👤 Admin :</b> {mention}

<blockquote expandable>
Select an option below to manage the bot.
</blockquote>
"""

        await query.message.edit_caption(

            caption=text,

            reply_markup=settings_buttons(),

        )

        await query.answer()

        return

    # ==========================================================
    # IGNORE SAME BUTTON SPAM
    # ==========================================================

    if data == "nothing":

        await query.answer()

        return

    # ==========================================================
    # UNKNOWN CALLBACK
    # ==========================================================

    await query.answer(

        "⚠️ Unknown Button.",

        show_alert=False

          )
              # ==========================================================
    # FUTURE CALLBACK ROUTER
    # ==========================================================

    if data.startswith("fsub_"):

        await query.answer(
            "🔒 Force Subscribe Panel (Coming in Phase 2)",
            show_alert=True
        )
        return

    if data.startswith("broadcast_"):

        await query.answer(
            "📢 Broadcast Panel (Coming in Phase 3)",
            show_alert=True
        )
        return

    if data.startswith("admin_"):

        await query.answer(
            "👑 Admin Panel (Coming Soon)",
            show_alert=True
        )
        return

    if data.startswith("ban_"):

        await query.answer(
            "🚫 Ban Panel (Coming Soon)",
            show_alert=True
        )
        return

    if data.startswith("status_"):

        await query.answer(
            "📊 Status Panel (Coming Soon)",
            show_alert=True
        )
        return

    if data.startswith("genlink_"):

        await query.answer(
            "🔗 Link Generator (Coming Soon)",
            show_alert=True
        )
        return

    if data.startswith("batch_"):

        await query.answer(
            "📦 Batch Generator (Coming Soon)",
            show_alert=True
        )
        return

    # ==========================================================
    # INVALID CALLBACK
    # ==========================================================

    await query.answer(
        "⚠️ Invalid Callback!",
        show_alert=False
  )
  

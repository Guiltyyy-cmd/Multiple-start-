"""
==========================================================
ONICORE BOTS

Bot Name  : Jhaplupirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

Buttons Manager
Production Ready
Fully Commented

==========================================================
"""

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


# ==========================================================
# Start Buttons
# ==========================================================

def start_buttons(is_admin: bool = False):
    """
    Returns start menu buttons.

    Parameters:
        is_admin : bool

    Returns:
        InlineKeyboardMarkup
    """

    buttons = [

        [
            InlineKeyboardButton(
                "📖 𝗔𝗕𝗢𝗨𝗧",
                callback_data="about"
            ),

            InlineKeyboardButton(
                "📢 𝗖𝗛𝗔𝗡𝗡𝗘𝗟𝗦",
                callback_data="channels"
            )

        ]

    ]

    # Show Settings only to Admin / Owner
    if is_admin:

        buttons.append(
            [

                InlineKeyboardButton(
                    "⚙️ 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦",
                    callback_data="settings"
                )

            ]
        )

    buttons.append(
        [

            InlineKeyboardButton(
                "❌ 𝗖𝗟𝗢𝗦𝗘",
                callback_data="close"
            )

        ]
    )

    return InlineKeyboardMarkup(buttons)


# ==========================================================
# About Buttons
# ==========================================================

def about_buttons(is_admin: bool = False):
    """
    About Panel Buttons
    """

    rows = [

        [

            InlineKeyboardButton(
                "◀️ 𝗕𝗔𝗖𝗞",
                callback_data="back_start"
            ),

            InlineKeyboardButton(
                "📢 𝗖𝗛𝗔𝗡𝗡𝗘𝗟𝗦",
                callback_data="channels"
            )

        ],

        [

            InlineKeyboardButton(
                "❌ 𝗖𝗟𝗢𝗦𝗘",
                callback_data="close"
            )

        ]

    ]

    return InlineKeyboardMarkup(rows)


# ==========================================================
# Channels Buttons
# ==========================================================

def channels_buttons(is_admin=False):
    """
    Channel Panel Buttons
    """

    rows = [

        [

            InlineKeyboardButton(
                "◀️ 𝗕𝗔𝗖𝗞",
                callback_data="back_start"
            ),

            InlineKeyboardButton(
                "📖 𝗔𝗕𝗢𝗨𝗧",
                callback_data="about"
            )

        ],

        [

            InlineKeyboardButton(
                "❌ 𝗖𝗟𝗢𝗦𝗘",
                callback_data="close"
            )

        ]

    ]

    return InlineKeyboardMarkup(rows)


# ==========================================================
# Force Subscribe Buttons
# ==========================================================

def fsub_buttons(start_parameter: str = ""):
    """
    Creates Force Subscribe Buttons
    """

    rows = []

    for channel in config.FORCE_SUB_CHANNELS:

        rows.append(

            [

                InlineKeyboardButton(

                    text=f"📢 {channel['name']}",

                    url=channel["link"]

                )

            ]

        )

    rows.append(

        [

            InlineKeyboardButton(

                "🔄 𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡",

                callback_data=f"try_again:{start_parameter}"

            )

        ]

    )

    return InlineKeyboardMarkup(rows)

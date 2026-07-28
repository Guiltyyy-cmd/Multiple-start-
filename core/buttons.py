"""
==========================================================
ONICORE BOTS

Bot Name  : JhapluPirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

buttons.py

All Inline Keyboard Buttons

==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pyrogram.types import (

    InlineKeyboardButton,
    InlineKeyboardMarkup

)

import config


# ==========================================================
# Start Buttons
# ==========================================================

def start_buttons(admin: bool = False):

    """
    Start Menu Buttons

    User:
    About
    Channels
    Close

    Admin:
    About
    Channels
    Settings
    Close
    """

    keyboard = [

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

    if admin:

        keyboard.append(

            [

                InlineKeyboardButton(

                    "⚙️ 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦",

                    callback_data="settings"

                )

            ]

        )

    keyboard.append(

        [

            InlineKeyboardButton(

                "❌ 𝗖𝗟𝗢𝗦𝗘",

                callback_data="close"

            )

        ]

    )

    return InlineKeyboardMarkup(keyboard)
    # ==========================================================
# About Buttons
# ==========================================================

def about_buttons(admin: bool = False):

    """
    About Panel Buttons
    """

    keyboard = [

        [

            InlineKeyboardButton(

                "📢 𝗖𝗛𝗔𝗡𝗡𝗘𝗟𝗦",

                callback_data="channels"

            )

        ],

        [

            InlineKeyboardButton(

                "◀️ 𝗕𝗔𝗖𝗞",

                callback_data="back_start"

            ),

            InlineKeyboardButton(

                "❌ 𝗖𝗟𝗢𝗦𝗘",

                callback_data="close"

            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================================================
# Channels Buttons
# ==========================================================

def channels_buttons(admin: bool = False):

    """
    Channels Panel Buttons
    """

    keyboard = [

        [

            InlineKeyboardButton(

                "📖 𝗔𝗕𝗢𝗨𝗧",

                callback_data="about"

            )

        ],

        [

            InlineKeyboardButton(

                "◀️ 𝗕𝗔𝗖𝗞",

                callback_data="back_start"

            ),

            InlineKeyboardButton(

                "❌ 𝗖𝗟𝗢𝗦𝗘",

                callback_data="close"

            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)
    # ==========================================================
# Settings Buttons
# ==========================================================

def settings_buttons():

    """
    Admin Settings Panel
    """

    keyboard = [

        [

            InlineKeyboardButton(

                "🔒 𝗙𝗦𝗨𝗕 𝗣𝗔𝗡𝗘𝗟",

                callback_data="fsub_panel"

            )

        ],

        [

            InlineKeyboardButton(

                "📊 𝗦𝗧𝗔𝗧𝗨𝗦",

                callback_data="status_panel"

            ),

            InlineKeyboardButton(

                "📢 𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧",

                callback_data="broadcast_panel"

            )

        ],

        [

            InlineKeyboardButton(

                "👑 𝗔𝗗𝗠𝗜𝗡𝗦",

                callback_data="admin_panel"

            ),

            InlineKeyboardButton(

                "🚫 𝗕𝗔𝗡",

                callback_data="ban_panel"

            )

        ],

        [

            InlineKeyboardButton(

                "◀️ 𝗕𝗔𝗖𝗞",

                callback_data="back_start"

            ),

            InlineKeyboardButton(

                "❌ 𝗖𝗟𝗢𝗦𝗘",

                callback_data="close"

            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================================================
# Common Close Button
# ==========================================================

def close_button():

    """
    Single Close Button
    """

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    "❌ 𝗖𝗟𝗢𝗦𝗘",

                    callback_data="close"

                )

            ]

        ]

    )


# ==========================================================
# Common Back Button
# ==========================================================

def back_button():

    """
    Single Back Button
    """

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    "◀️ 𝗕𝗔𝗖𝗞",

                    callback_data="back_start"

                )

            ]

        ]

    )
    

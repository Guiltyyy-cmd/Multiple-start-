"""
==========================================================
ONICORE BOTS

Bot Name  : Jhaplupirobot
Developer : @BlurpleOg
Marketing : #onicore_bots

Animation Cooldown Manager
Production Ready
Fully Commented

==========================================================
"""

# ==========================================================
# Required Imports
# ==========================================================

import time
import config

# ==========================================================
# User Cooldown Cache
# ==========================================================
#
# Stores:
#
# {
#     user_id : last_animation_timestamp
# }
#
# ==========================================================

_animation_cache = {}


# ==========================================================
# Check Animation Cooldown
# ==========================================================

def can_show_animation(user_id: int):
    """
    Checks whether the animation
    should be shown.

    Returns
    -------
    True  -> Show animation

    False -> Skip animation
    """

    current_time = int(time.time())

    last_time = _animation_cache.get(user_id)

    # User never saw animation
    if last_time is None:
        return True

    elapsed = current_time - last_time

    return elapsed >= config.ANIMATION_COOLDOWN


# ==========================================================
# Save Animation Timestamp
# ==========================================================

def update_animation_time(user_id: int):
    """
    Saves current timestamp
    after animation completes.
    """

    _animation_cache[user_id] = int(time.time())


# ==========================================================
# Remaining Cooldown
# ==========================================================

def remaining_time(user_id: int):
    """
    Returns remaining cooldown
    in seconds.
    """

    current_time = int(time.time())

    last_time = _animation_cache.get(user_id)

    if last_time is None:
        return 0

    remaining = config.ANIMATION_COOLDOWN - (
        current_time - last_time
    )

    if remaining < 0:
        remaining = 0

    return remaining


# ==========================================================
# Remove User Cache
# ==========================================================

def clear_user(user_id: int):
    """
    Removes a user from cache.
    """

    _animation_cache.pop(user_id, None)


# ==========================================================
# Clear All Cache
# ==========================================================

def clear_all():
    """
    Clears complete cooldown cache.
    """

    _animation_cache.clear()

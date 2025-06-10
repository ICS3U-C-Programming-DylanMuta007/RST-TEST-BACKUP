#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :June 2025
# Space aliens in a pybadge

SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 10
TOTAL_NUMBER_OF_LASERS = 5
SHIP_SPEED = 6
ALIEN_SPEED = 1
LASER_SPEED = 2
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 30
SPRITE_MOVEMENT_SPEED = 2


# Using for button state
button_state = {"button_up": "up",
                "button_just_pressed": "just pressed",
                "button_still_pressed": "still pressed",
                "button_realeased": "released"
                }

# palette
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
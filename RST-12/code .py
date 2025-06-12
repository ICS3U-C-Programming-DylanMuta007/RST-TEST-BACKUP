#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :June 2025
# Space alienss in a pybadge

import ugame  # type: ignore
import stage  # type: ignore
import constant
import time
import random

def splash_scene():
    # This funtion is the splash game

    # get the coin sound
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # image banks for circuit python
    mt_background_image = stage.Bank.from_bmp16("mt_game_studio.bmp")

    background = stage.Grid(mt_background_image, constant.SCREEN_X, 
                            constant.SCREEN_Y)


    # Set the background to image 0 in the image bank 
    background = stage.Grid(mt_background_image, constant.SCREEN_X, constant.SCREEN_Y)

    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white


    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white


    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white


    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white

    #creates a stage for the background to show up on
    # and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constant.FPS)
    game.layers = [background]

    ## render the background and initial location of sprite list
    game.render_block()

    while True:
        # Wait for 2 seconds 
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    # This funtion is the main game

    # image banks for circuit python
    background_image = stage.Bank.from_bmp16("space_alienss_background.bmp")

    # adds text objects
    text = []
    text1 = stage.Text(width = 29, height =12, font =None, palette =constant.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("I HATE THIS")
    text.append(text1)

    text2 = stage.Text(width = 29, height =12, font =None, palette =constant.RED_PALETTE, buffer=None)
    text2.move(20, 10)
    text2.text("PRESS START")
    text.append(text2)

    # Set the background to image 0 in the image bank 
    # set size to 10 X 8 tiles of 16 X 16
    background = stage.Grid(background_image, constant.SCREEN_GRID_X, constant.SCREEN_GRID_Y)

    

    #creates a stage for the background to show up on
    # and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constant.FPS)
    game.layers = text + [background]

    ## render the background and initial location of sprite list
    game.render_block()

    while True:
        # user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_START != 0:
            game_scene()

        # redraws the sprites
        game.tick()

def game_scene():
    # This funtion is the main game

    score = 0

    score_text = stage.TEXT(width = 29, height = 14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("Score: {0}" .format(score))

    def show_alien():
        # this finctio takes an alien from off screen and moves it on screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randit(0 + constant.SPRITE_SIZE, 
                                                        constant.SCREEN_X - constant.SPRITE_SIZE), 
                                            constant.OFF_TOP_SCREEN)
                break

    # image banks for circuit python
    background_image = stage.Bank.from_bmp16("space_alienss_background.bmp")
    sprite_image = stage.Bank.from_bmp16("space_alienss.bmp")

    # buttonsthat you wnat to keep state information on
    a_button = constant.button_state["button_up"]
    b_button = constant.button_state["button_up"]
    start_button = constant.button_state["button_up"]
    select_button = constant.button_state["button_up"]

    # Get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Boom sound
    boom_sound = open("boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Set the background to image 0 in the image bank 
    # set size to 10 X 8 tiles of 16 X 16
    background = stage.Grid(background_image, constant.SCREEN_GRID_X,
                             constant.SCREEN_GRID_Y)

    for x_location in range(constant.SCREEN_GRID_X):
        for y_location in range(constant.SCREEN_GRID_Y):
            tile_picked = random.randint(1,3)
            background.tile(x_location, y_location, tile_picked)
    
    # A sprite that will updated every frame
    ship = stage.Sprite(sprite_image, 5, 75, constant.SCREEN_Y - (2* constant.SPRITE_SIZE))

    # Creates list if aliens 
    aliens = []
    for alien_number in range (constant.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(sprite_image, 9,
                                      constant.OFF_SCREEN_X,
                                      constant.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    #Place 1 alien on the screen
    show_alien()
    
    # Creates list if lasers for when we shoot
    lasers = []
    for laser_number in range(constant.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.sprite(sprite_image, 10,
                                      constant.OFF_SCREEN_X,
                                      constant.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    #creates a stage for the background to show up on
    # and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constant.FPS)
    game.layers = [score_text] + lasers + [ship] + aliens + [background]

    ## render the background and initial location of sprite list
    game.render_block()

    while True:
        # user input
        keys = ugame.buttons.get_pressed()
        
        # A button
        if keys & ugame.K_O != 0:
            if a_button == constant.button_state["button_up"]:
                a_button = constant.button_state["button_just_pressed"]
            elif a_button == constant.button_state["button_just_pressed"]:
                a_button = constant.button_state["button_still_pressed"]

        else:
            if a_button == constant.button_state["button_still_pressed"]:
                a_button = constant.button_state['button_released']
            else:
                a_button = constant.button_state["button_up"]
            
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass

        # Rigth button
        if keys & ugame.K_RIGHT:
            if ship.x <= constant.SCREEN_X - constant.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constant.SCREEN_X - constant.SPRITE_SIZE, ship.y)

        # Left button
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)


        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        if a_button == constant.button_state["button_just_pressed"]:
            # shoots a laser, if we have enought power
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # each frame move the lasers up, that have been fired
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, 
                                          lasers[laser_number].y - 
                                          constant.LASER_SPEED)
                
                if lasers[laser_number].y < constant.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constant.OFF_SCREEN_X,
                                              constant.OFF_SCREEN_Y)
        
        # each frame move the aliens down, that are on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x,
                                          aliens[alien_number].y +
                                          constant.ALIEN_SPEED)
                
            if aliens[alien_number].y > constant.SCREEN_Y:
                aliens[alien_number].move(constant.OFF_SCREEN_X,
                                          constant.OFF_SCREEN_Y)
                show_alien()
                score -= 1

                if score < 0:
                    score = 0
                score_text.clear()
                score_text.cursor(0,0)
                score_text.move(1,1)
                score_text.text("Score: {0}" .format(score))
                
            
            # each frame check if any of the lasers are colliding with anmy of the aliens 
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x > 0:
                    for alien_number in range(len(aliens)):
                        if aliens[alien_number].x > 0:
                            if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                             lasers[laser_number].x + 11, lasers[laser_number].y + 12, 
                                             aliens[alien_number].x + 1, aliens[alien_number].y, 
                                             aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                                #you hit an alien
                                aliens[alien_number].move(constant.OFF_SCREEN_X, constant.OFF_SCREEN_Y)
                                lasers[laser_number].move(constant.OFF_SCREEN_X, constant.OFF_SCREEN_Y)
                                sound.play(boom_sound)
                                show_alien()
                                show_alien()
                                score = score + 1
                                score_text.clear()
                                score_text.cursor(0,0)
                                score_text.move(1,1)
                                score_text.text("Score: {0}" .format(score))

        # redraws the sprites
        game.render_sprites(lasers + [ship] + aliens)
        game.tick()
    
if __name__ == "__main__":
    splash_scene() # type: ignore
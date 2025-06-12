#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :June 2025
# Space aliens in a pybadge

import ugame  # type: ignore
import stage  # type: ignore
import constant

def menu_scene():
    # This funtion is the main game

    # image banks for circuit python
    background_image = stage.Bank.from_bmp16("space_aliens_background.bmp")

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

    # image banks for circuit python
    background_image = stage.Bank.from_bmp16("space_aliens_background.bmp")
    sprite_image = stage.Bank.from_bmp16("space_aliens.bmp")

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

    # Set the background to image 0 in the image bank 
    # set size to 10 X 8 tiles of 16 X 16
    background = stage.Grid(background_image, constant.SCREEN_GRID_X, constant.SCREEN_GRID_Y)
    
    # A sprite that will updated every frame
    ship = stage.Sprite(sprite_image, 5, 75, constant.SCREEN_Y - (2* constant.SPRITE_SIZE))

    alien = stage.Sprite(sprite_image, 9, 
                         int(constant.SCREEN_GRID_X / 2 - constant.SPRITE_SIZE / 2), 
                         16)
    

    #creates a stage for the background to show up on
    # and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constant.FPS)
    game.layers = [ship] + [alien] + [background]

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
            sound.play(pew_sound)

        # redraws the sprites
        game.render_sprites([ship] + [alien])
        game.tick()
    
if __name__ == "__main__":
    menu_scene() # type: ignore
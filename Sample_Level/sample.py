import pygame as pg

"""
Created game dimensions and background color

"""

(width, height) = (800, 700)
background_color = (205, 207, 209)


gameDisplay = pg.display.set_mode((width, height))
gameDisplay.fill(background_color)

"""
Import and load a set of bricks to be used as level border
"""
brick = pg.image.load('brick.png')
brick_image = pg.transform.scale(brick, (40, 40))
gameDisplay.blit(brick_image, (60, 0))
gameDisplay.blit(brick_image, (60, 30))
gameDisplay.blit(brick_image, (60, 60))
gameDisplay.blit(brick_image, (60, 90))
gameDisplay.blit(brick_image, (60, 120))
gameDisplay.blit(brick_image, (60, 150))
gameDisplay.blit(brick_image, (60, 180))
gameDisplay.blit(brick_image, (60, 210))
gameDisplay.blit(brick_image, (60, 240))
gameDisplay.blit(brick_image, (60, 270))
gameDisplay.blit(brick_image, (60, 300))
gameDisplay.blit(brick_image, (90, 300))
gameDisplay.blit(brick_image, (120, 300))
gameDisplay.blit(brick_image, (120, 330))
gameDisplay.blit(brick_image, (120, 360))
gameDisplay.blit(brick_image, (120, 390))
gameDisplay.blit(brick_image, (120, 420))
gameDisplay.blit(brick_image, (120, 450))
gameDisplay.blit(brick_image, (120, 480))
gameDisplay.blit(brick_image, (120, 510))
gameDisplay.blit(brick_image, (120, 540))
gameDisplay.blit(brick_image, (120, 570))
gameDisplay.blit(brick_image, (120, 600))
gameDisplay.blit(brick_image, (120, 630))
gameDisplay.blit(brick_image, (150, 630))
gameDisplay.blit(brick_image, (180, 630))
gameDisplay.blit(brick_image, (210, 630))
gameDisplay.blit(brick_image, (240, 630))
gameDisplay.blit(brick_image, (270, 630))
gameDisplay.blit(brick_image, (300, 630))
gameDisplay.blit(brick_image, (330, 630))
gameDisplay.blit(brick_image, (360, 630))
gameDisplay.blit(brick_image, (390, 630))
gameDisplay.blit(brick_image, (420, 630))
gameDisplay.blit(brick_image, (450, 630))
gameDisplay.blit(brick_image, (480, 630))
gameDisplay.blit(brick_image, (510, 630))
gameDisplay.blit(brick_image, (540, 630))
gameDisplay.blit(brick_image, (570, 630))
gameDisplay.blit(brick_image, (510, 630))
gameDisplay.blit(brick_image, (540, 630))
gameDisplay.blit(brick_image, (570, 630))
gameDisplay.blit(brick_image, (600, 630))
gameDisplay.blit(brick_image, (630, 630))
gameDisplay.blit(brick_image, (660, 630))
gameDisplay.blit(brick_image, (660, 0))
gameDisplay.blit(brick_image, (660, 30))
gameDisplay.blit(brick_image, (660, 60))
gameDisplay.blit(brick_image, (660, 90))
gameDisplay.blit(brick_image, (660, 120))
gameDisplay.blit(brick_image, (660, 150))
gameDisplay.blit(brick_image, (660, 180))
gameDisplay.blit(brick_image, (660, 210))
gameDisplay.blit(brick_image, (660, 240))
gameDisplay.blit(brick_image, (660, 270))
gameDisplay.blit(brick_image, (660, 300))
gameDisplay.blit(brick_image, (660, 300))
gameDisplay.blit(brick_image, (660, 330))
gameDisplay.blit(brick_image, (660, 360))
gameDisplay.blit(brick_image, (660, 390))
gameDisplay.blit(brick_image, (660, 420))
gameDisplay.blit(brick_image, (660, 450))
gameDisplay.blit(brick_image, (660, 480))
gameDisplay.blit(brick_image, (660, 510))
gameDisplay.blit(brick_image, (660, 540))
gameDisplay.blit(brick_image, (660, 570))
gameDisplay.blit(brick_image, (660, 600))
gameDisplay.blit(brick_image, (660, 630))
gameDisplay.blit(brick_image, (60, 0))
gameDisplay.blit(brick_image, (90, 0))
gameDisplay.blit(brick_image, (120, 0))
gameDisplay.blit(brick_image, (150, 0))
gameDisplay.blit(brick_image, (180, 0))
gameDisplay.blit(brick_image, (210, 0))
gameDisplay.blit(brick_image, (240, 0))
gameDisplay.blit(brick_image, (270, 0))
gameDisplay.blit(brick_image, (300, 0))
gameDisplay.blit(brick_image, (330, 0))
gameDisplay.blit(brick_image, (360, 0))
gameDisplay.blit(brick_image, (390, 0))
gameDisplay.blit(brick_image, (420, 0))
gameDisplay.blit(brick_image, (450, 0))
gameDisplay.blit(brick_image, (480, 0))
gameDisplay.blit(brick_image, (510, 0))
gameDisplay.blit(brick_image, (540, 0))
gameDisplay.blit(brick_image, (570, 0))
gameDisplay.blit(brick_image, (600, 0))
gameDisplay.blit(brick_image, (630, 0))
gameDisplay.blit(brick_image, (90, 180))
gameDisplay.blit(brick_image, (120, 180))
gameDisplay.blit(brick_image, (150, 180))
gameDisplay.blit(brick_image, (180, 180))
gameDisplay.blit(brick_image, (210, 180))
gameDisplay.blit(brick_image, (210, 210))
gameDisplay.blit(brick_image, (240, 180))
gameDisplay.blit(brick_image, (240, 210))
gameDisplay.blit(brick_image, (240, 240))
gameDisplay.blit(brick_image, (240, 270))
gameDisplay.blit(brick_image, (240, 300))
gameDisplay.blit(brick_image, (240, 330))
gameDisplay.blit(brick_image, (240, 360))
gameDisplay.blit(brick_image, (240, 390))

"""
Load the images of the box and the character
"""

box_non = pg.image.load('box.png')
box = pg.transform.scale(box_non, (40, 40))
pressure_plate = pg.image.load('pressure.png')
pressure_image = pg.transform.scale(pressure_plate, (15, 15))
player_image = pg.image.load('character.png')
player = pg.transform.scale(player_image, (60, 60))
gameDisplay.blit(player, (350, 70))
gameDisplay.blit(pressure_image, (120, 240))
gameDisplay.blit(box, (450, 450))


"""
Begin running the game
"""
pg.display.flip()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

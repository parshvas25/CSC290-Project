import pygame as pg

(width, height) = (800, 700)
background_color = (0,0,0)


gameDisplay = pg.display.set_mode((width, height))
gameDisplay.fill(background_color)

"""
Import and load a set of bricks to be used as level border
"""
brick = pg.image.load('brick.png')
brick_image = pg.transform.scale(brick, (40,40))
gameDisplay.blit(brick_image, (0,0))
gameDisplay.blit(brick_image, (0,30))
gameDisplay.blit(brick_image, (0,60))
gameDisplay.blit(brick_image, (0,90))
gameDisplay.blit(brick_image, (0,120))
gameDisplay.blit(brick_image, (0,150))
gameDisplay.blit(brick_image, (0,180))
gameDisplay.blit(brick_image, (0,210))
gameDisplay.blit(brick_image, (0,240))
gameDisplay.blit(brick_image, (0,270))
gameDisplay.blit(brick_image, (0,300))
gameDisplay.blit(brick_image, (30,300))
gameDisplay.blit(brick_image, (60,300))
gameDisplay.blit(brick_image, (60,330))
gameDisplay.blit(brick_image, (60,360))
gameDisplay.blit(brick_image, (60,390))
gameDisplay.blit(brick_image, (60,420))
gameDisplay.blit(brick_image, (60,450))
gameDisplay.blit(brick_image, (60,480))
gameDisplay.blit(brick_image, (60,510))
gameDisplay.blit(brick_image, (60,540))
gameDisplay.blit(brick_image, (60,570))
gameDisplay.blit(brick_image, (60,600))
gameDisplay.blit(brick_image, (60,630))
gameDisplay.blit(brick_image, (90,630))
gameDisplay.blit(brick_image, (120,630))
gameDisplay.blit(brick_image, (150,630))
gameDisplay.blit(brick_image, (180,630))
gameDisplay.blit(brick_image, (210,630))
gameDisplay.blit(brick_image, (240,630))
gameDisplay.blit(brick_image, (240,630))
gameDisplay.blit(brick_image, (270,630))
gameDisplay.blit(brick_image, (300,630))
gameDisplay.blit(brick_image, (330,630))
gameDisplay.blit(brick_image, (360,630))
gameDisplay.blit(brick_image, (390,630))
gameDisplay.blit(brick_image, (420,630))
gameDisplay.blit(brick_image, (450,630))
gameDisplay.blit(brick_image, (480,630))
gameDisplay.blit(brick_image, (510,630))
gameDisplay.blit(brick_image, (540,630))
gameDisplay.blit(brick_image, (570,630))
gameDisplay.blit(brick_image, (600,630))
gameDisplay.blit(brick_image, (630,630))
gameDisplay.blit(brick_image, (660,630))
gameDisplay.blit(brick_image, (660,0))
gameDisplay.blit(brick_image, (660,30))
gameDisplay.blit(brick_image, (660,60))
gameDisplay.blit(brick_image, (660,90))
gameDisplay.blit(brick_image, (660,120))
gameDisplay.blit(brick_image, (660,150))
gameDisplay.blit(brick_image, (660,180))
gameDisplay.blit(brick_image, (660,210))
gameDisplay.blit(brick_image, (660,240))
gameDisplay.blit(brick_image, (660,270))
gameDisplay.blit(brick_image, (660,300))
gameDisplay.blit(brick_image, (660,300))
gameDisplay.blit(brick_image, (660,330))
gameDisplay.blit(brick_image, (660,360))
gameDisplay.blit(brick_image, (660,390))
gameDisplay.blit(brick_image, (660,420))
gameDisplay.blit(brick_image, (660,450))
gameDisplay.blit(brick_image, (660,480))
gameDisplay.blit(brick_image, (660,510))
gameDisplay.blit(brick_image, (660,540))
gameDisplay.blit(brick_image, (660,570))
gameDisplay.blit(brick_image, (660,600))
gameDisplay.blit(brick_image, (660,630))

player_image = pg.image.load('character.png')
player = pg.transform.scale(player_image,(60,60))
gameDisplay.blit(player,(350,70))



pg.display.flip()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

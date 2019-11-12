import pygame
from pygame import *

# Global constants

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

def get_sprite(sprite_name):
    image = pygame.image.load("Sprites\\" +sprite_name)
    return image

class Player(pygame.sprite.Sprite):

    #Construct the player class
    def __init__(self, x, y):
        super().__init__()

        # TODO: CHANGE BASE RECTANGLE CHARACTER TO SPRITE
        self.image = get_sprite("character.png")


        # Set the top left position of the location to the x,y coordinate passed in
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


    def update(self):
        """Used to update the players position"""
        pass

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        this.image = pygame.image.load("Sprites/brick.jpg")
        this.x = x
        this.y = y
    def blit():
        screen.blit(this.image,x, y )


        
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Test")

sprites_list = pygame.sprite.Group()
player = Player(50,50)
sprites_list.add(player)

clock = pygame.time.Clock()

gameRunning = True

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    sprites_list.update()
    sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()

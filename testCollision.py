import pygame
from pygame import *
import numpy as np

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
MOVE_DISTANCE = 50

# Grid block size
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50

def get_sprite(sprite_name):
    image = pygame.image.load("Images/" +sprite_name)
    return image
    
class Player(pygame.sprite.Sprite):

    #Construct the player class
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.transform.scale(get_sprite("character.png"),(60,60))

        # Set the top left position of the location to the x,y coordinate passed in
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.dir_x = 0
        self.dir_y = 0

    def move(self, x, y):
        """Used to update the players position"""
        newX = self.dir_x + x
        newY = self.dir_y + y

        self.dir_x += x
        self.dir_y += y
        self.change_sprite()

    def change_sprite(self):
        if self.dir_x > 0:
            self.image = pygame.transform.scale(get_sprite("character-right.png"),(60,60))
        elif self.dir_x < 0:
            self.image = pygame.transform.scale(get_sprite("character.png"),(60,60))

    def update(self, walls):
        """Used to update the players position"""
        old_x = self.rect.x
        old_y = self.rect.y
        self.rect.x += self.dir_x
        self.rect.y += self.dir_y

        # Check if we collided with something
        for wall in walls:
            if pygame.sprite.spritecollide(self, wall):
                self.rect.x=old_x
                self.rect.y=old_y

                

        self.dir_x = 0
        self.dir_y = 0

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = get_sprite("brick.png")
        self.x = x
        self.y = y
    def appear(self):
        brick_image = pygame.transform.scale(self.image, (40, 40))
        screen.blit(brick_image,(self.x,self.y))


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 60, 60)
        self.image  = pygame.surface.Surface((60, 60))
        self.image.fill(WHITE)

    def draw(self, screen):
        screen.blit(self.img, self.rect)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sokoban")

player = Player(400,400)
tile = Tile(50,50)

player_group = pygame.sprite.Group()
player_group.add(player)
wall_list = pygame.sprite.Group()
wall_list.add(tile)

gameRunning = True
isMoving = False
clock = pygame.time.Clock()

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        elif event.type == pygame.KEYDOWN:
            if not isMoving:
                isMoving = True
                if event.key == pygame.K_LEFT:
                    player.move(-MOVE_DISTANCE, 0)
                elif event.key == pygame.K_RIGHT:
                    player.move(MOVE_DISTANCE, 0)
                elif event.key == pygame.K_UP:
                    player.move(0, -MOVE_DISTANCE)
                elif event.key == pygame.K_DOWN:
                    player.move(0, MOVE_DISTANCE)
        
    screen.fill(BLACK)
    player.update(wall_list)
    player_group.draw(screen)
    wall_list.draw(screen)
    pygame.display.flip()
    
    if(isMoving):
        pygame.time.delay(100)
        isMoving = False
    
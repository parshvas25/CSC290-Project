import pygame
from pygame import *

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
MOVE_DISTANCE = 50

def get_sprite(sprite_name):
    image = pygame.image.load("Images/" +sprite_name)
    return image

class Player(pygame.sprite.Sprite):

    #Construct the player class
    def __init__(self, x, y):
        super().__init__()

        # TODO: CHANGE BASE RECTANGLE CHARACTER TO SPRITE
        self.image = pygame.transform.scale(get_sprite("character.png"),(60,60))


        # Set the top left position of the location to the x,y coordinate passed in
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.dir_x = 0
        self.dir_y = 0

    def move(self, x, y):
        """Used to update the players position"""
        self.dir_x += x
        self.dir_y += y
        self.change_sprite()

    def change_sprite(self):
        if self.dir_x > 0:
            self.image = pygame.transform.scale(get_sprite("character-right.png"),(60,60))
        elif self.dir_x < 0:
            self.image = pygame.transform.scale(get_sprite("character.png"),(60,60))


    def update(self):
        """Used to update the players position"""
        self.rect.x += self.dir_x
        self.rect.y += self.dir_y

        self.dir_x = 0
        self.dir_y = 0

# This class is responsible for creating the Box Boundaries for each level
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("Images/brick.png")
        self.x = x
        self.y = y
    def appear(self):
        brick_image = pygame.transform.scale(self.image, (40, 40))
        screen.blit(brick_image,(self.x,self.y))

# This nested array is responsible for representing each level as a set of coor-
#dinate values the box will be appear on the screan
levels = [[[0,0], [30,0], [60,0]]]



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sokoban")

sprites_list = pygame.sprite.Group()
player = Player(400,400)
sprites_list.add(player)

gameRunning = True
isMoving = False
clock = pygame.time.Clock()

current_level = 1

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

    sprites_list.update()

    screen.fill(BLACK)
    sprites_list.draw(screen)
    pygame.display.flip()
    if(isMoving):
        pygame.time.delay(100)
        isMoving = False


pygame.quit()
quit()

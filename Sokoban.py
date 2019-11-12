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
    image = pygame.image.load("Images\\" +sprite_name)
    return image

class Player(pygame.sprite.Sprite):

    #Construct the player class
    def __init__(self, x, y):
        super().__init__()
<<<<<<< HEAD

        # TODO: CHANGE BASE RECTANGLE CHARACTER TO SPRITE
        self.image = get_sprite("character.png")


=======
 
        # Sets the player movement to the sprite png 
        self.image = pygame.transform.scale(get_sprite("character.png"),(60,60))
 
>>>>>>> 281290dbdec61e26fe086543e7c9e586b9d796a4
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


<<<<<<< HEAD

=======
>>>>>>> 281290dbdec61e26fe086543e7c9e586b9d796a4
    def update(self):
        """Used to update the players position"""
        self.rect.x += self.dir_x
        self.rect.y += self.dir_y

        self.dir_x = 0
        self.dir_y = 0
        

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        this.image = pygame.image.load("Sprites/brick.jpg")
        this.x = x
        this.y = y
    def blit():
        screen.blit(this.image,x, y )


        
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sokoban")

sprites_list = pygame.sprite.Group()
player = Player(400,400)
sprites_list.add(player)

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
                
    sprites_list.update()
<<<<<<< HEAD
    sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
=======
    screen.fill(BLACK)
    sprites_list.draw(screen) 
    pygame.display.flip() 
    if(isMoving):
        pygame.time.delay(100)
        isMoving = False
>>>>>>> 281290dbdec61e26fe086543e7c9e586b9d796a4

pygame.quit()
quit()

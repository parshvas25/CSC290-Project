import pygame
from pygame import *

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#PNG IMAGES
PLAYER_LEFT = "player-left.png"
PLAYER_RIGHT = "player-right.png"
WALL_IMAGE = "wall.png"
CRATE_IMAGE = "crate.png"
STORAGE_IMAGE = "storage.png"

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
MOVE_DISTANCE = 50

# Grid block size
BLOCK_SIZE = 50


def get_sprite(sprite_name):
    image = pygame.image.load("Images/" +sprite_name)
    return image

def main():
    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.transform.scale(get_sprite(PLAYER_LEFT),(BLOCK_SIZE,BLOCK_SIZE))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            # Direction that the player will travel
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
                self.image = pygame.transform.scale(get_sprite(PLAYER_RIGHT),(BLOCK_SIZE,BLOCK_SIZE))
            elif self.dir_x < 0:
                self.image = pygame.transform.scale(get_sprite(PLAYER_LEFT),(BLOCK_SIZE,BLOCK_SIZE))

        def update(self, walls, crates):
            """Used to update the players position"""
            old_x = self.rect.x
            old_y = self.rect.y
            self.rect.x += self.dir_x
            self.rect.y += self.dir_y

            # Check if we collided with something
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.x=old_x
                    self.rect.y=old_y

            for crate in crates:
                if self.rect.colliderect(crate.rect):
                    #check if u can push compared to every crate except itself
                    tempCrateList = list(crates)
                    tempCrateList.remove(crate)
                    if not (crate.move(self.dir_x, self.dir_y, walls, tempCrateList)):
                    #if you cant push move back
                        self.rect.x=old_x
                        self.rect.y=old_y


            self.dir_x = 0
            self.dir_y = 0

    class Crate(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.transform.scale(get_sprite(CRATE_IMAGE),(BLOCK_SIZE,BLOCK_SIZE))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def draw(self):
            screen.blit(self.image,(self.rect.x,self.rect.y))

        def move(self, dir_x, dir_y, walls, crates):
            old_x = self.rect.x
            old_y = self.rect.y
            self.rect.x += dir_x
            self.rect.y += dir_y
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.x = old_x
                    self.rect.y = old_y
                    return False
            for crate in crates:
                if self.rect.colliderect(crate.rect):
                    self.rect.x = old_x
                    self.rect.y = old_y
                    return False

            return True


    class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.transform.scale(get_sprite(WALL_IMAGE),(BLOCK_SIZE,BLOCK_SIZE))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def draw(self):
            screen.blit(self.image,(self.rect.x,self.rect.y))


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Sokoban")

    # MAKE PLAYER
    player = Player(400,400)
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # MAKE WALLS
    createWalls = []
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        createWalls.append(Wall(x,0))
        createWalls.append(Wall(x,SCREEN_HEIGHT - BLOCK_SIZE))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        createWalls.append(Wall(0,y))
        createWalls.append(Wall(SCREEN_WIDTH - BLOCK_SIZE, y))

    wall_list = pygame.sprite.Group()
    for wall in createWalls:
        wall_list.add(wall)

    # MAKE CRATES
    createCrates = []
    createCrates.append(Crate(100,150))
    createCrates.append(Crate(150,150))
    createCrates.append(Crate(400,150))
    createCrates.append(Crate(700,150))

    crate_list = pygame.sprite.Group()
    for crate in createCrates:
        crate_list.add(crate)

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

        screen.fill(BLACK) #Start draw

        player.update(wall_list, crate_list)
        player_group.draw(screen)
        wall_list.draw(screen)
        crate_list.draw(screen)

        pygame.display.flip() #End draw

        if(isMoving):
            pygame.time.delay(100)
            isMoving = False

if __name__ == "__main__":
    main()

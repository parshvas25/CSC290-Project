import pygame
from pygame import *
import os


# Global constants

# PNG IMAGES
PLAYER_LEFT = "player-left.png"
PLAYER_RIGHT = "player-right.png"
WALL_IMAGE = "wall.png"
CRATE_IMAGE = "crate.png"
STORAGE_IMAGE = "storage.png"

# Grid block size
BLOCK_SIZE = 50


def get_sprite(sprite_name):
    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath('..\\Resources\\Images', cur_path)
    image = pygame.image.load(new_path + "\\" + sprite_name)
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(get_sprite(PLAYER_LEFT),
                                            (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Direction that the player will travel
        self.dir_x = 0
        self.dir_y = 0

    def move(self, x, y):
        """Used to update the players position"""
        self.dir_x += x
        self.dir_y += y
        self.change_sprite()

    def change_sprite(self):
        if self.dir_x > 0:
            self.image = pygame.transform.scale(get_sprite(PLAYER_RIGHT),
                                                (BLOCK_SIZE, BLOCK_SIZE))
        elif self.dir_x < 0:
            self.image = pygame.transform.scale(get_sprite(PLAYER_LEFT),
                                                (BLOCK_SIZE, BLOCK_SIZE))

    def update(self, walls, crates, storages):
        """Used to update the players position"""
        old_x = self.rect.x
        old_y = self.rect.y
        self.rect.x += self.dir_x
        self.rect.y += self.dir_y

        # Check if we collided with something
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.rect.x = old_x
                self.rect.y = old_y

        for crate in crates:
            if self.rect.colliderect(crate.rect):
                # check if u can push compared to every crate except itself
                temp_crate_list = list(crates)
                temp_crate_list.remove(crate)
                if not (crate.move(self.dir_x, self.dir_y, walls, temp_crate_list, storages)):
                    # if you cant push move back
                    self.rect.x = old_x
                    self.rect.y = old_y

        self.dir_x = 0
        self.dir_y = 0


class Crate(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(get_sprite(CRATE_IMAGE),
                                            (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.stored = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, dir_x, dir_y, walls, crates, storages):
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
        for storage in storages:
            if self.rect.colliderect(storage.rect):
                self.stored = True
                break
            else:
                self.stored = False

        return True


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(get_sprite(WALL_IMAGE),
                                            (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Storage(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(get_sprite(STORAGE_IMAGE),
                                            (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

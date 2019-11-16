import pygame as pg
from typing import List
from level import Levels, LevelOne
import os

DIMENSION = (500, 500)
gameDisplay = pg.display.set_mode(DIMENSION)


def import_image() -> List:
    """
    Import the images and return them as a list
    :return: List of images
    """

    wall = pg.image.load(get_image_path("wall.png"))
    wall_image = pg.transform.scale(wall, (50, 70))

    crate = pg.image.load(get_image_path("crate.png"))
    crate_image = pg.transform.scale(crate, (50, 50))

    storage = pg.image.load(get_image_path("storage.png"))
    storage_image = pg.transform.scale(storage, (25, 25))

    player_left = pg.image.load(get_image_path("player-left.png"))
    player_left_image = pg.transform.scale(player_left, (50, 50))

    return [wall_image, crate_image, storage_image, player_left_image]


def get_image_path(image):
    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath('..\\Images\\'+image, cur_path)

    return new_path


def draw(level: Levels) -> None:
    """
    Draw the level on pygame
    """
    grid = level.grid
    wall_image, crate_image, storage_image, player_left_image = import_image()

    for i in range(10):
        for j in range(10):
            if grid[i][j] == level.WALL:
                gameDisplay.blit(wall_image, (i * 50, j * 50))
            if grid[i][j] == level.CRATE:
                gameDisplay.blit(crate_image, (i * 50, j * 55))
            if grid[i][j] == level.STORAGE:
                gameDisplay.blit(storage_image, (i * 55, j * 55))
            if grid[i][j] == level.PLAYER:
                gameDisplay.blit(player_left_image, (i * 50, j * 50))
    pg.display.flip()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


if __name__ == '__main__':
    level_one = LevelOne()
    draw(level_one)

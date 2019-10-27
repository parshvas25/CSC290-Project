import pygame as pg
from typing import List
from level import Levels, LevelOne

DIMENSION = (500, 500)
gameDisplay = pg.display.set_mode(DIMENSION)


def import_image() -> List:
    """
    Import the images and return them as a list
    :return: List of images
    """
    wall = pg.image.load('brick.png')
    wall_image = pg.transform.scale(wall, (50, 70))

    box = pg.image.load('box.png')
    box_image = pg.transform.scale(box, (50, 50))

    point = pg.image.load('pressure.png')
    point_image = pg.transform.scale(point, (25, 25))

    player = pg.image.load('character.png')
    player_image = pg.transform.scale(player, (50, 50))

    return [wall_image, box_image, point_image, player_image]


def draw(level: Levels) -> None:
    """
    Draw the level on pygame
    """
    grid = level.grid
    wall_image, box_image, point_image, player_image = import_image()

    for i in range(10):
        for j in range(10):
            if grid[i][j] == level.WALL:
                gameDisplay.blit(wall_image, (i * 50, j * 50))
            if grid[i][j] == level.BOX:
                gameDisplay.blit(box_image, (i * 50, j * 55))
            if grid[i][j] == level.POINT:
                gameDisplay.blit(point_image, (i * 55, j * 55))
            if grid[i][j] == level.PLAYER:
                gameDisplay.blit(player_image, (i * 50, j * 50))
    pg.display.flip()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


if __name__ == '__main__':
    level_one = LevelOne()
    draw(level_one)

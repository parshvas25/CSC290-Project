from typing import List

"""
Level layout for each level. Dimension is 10 by 10.
Outermost layer should be all walls. 
Each function will return a nested list consists of different types of objects
(e.g. wall, box, player, storage, and empty grid).
"""

W = "wall"
B = "box"
P = "player"
S = "storage"
E = "empty"


def level_one() -> List[List[str]]:
    """
    Level layout for level 1.
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, P, E, E, E, W, E, S, S, W])
    grid.append([W, E, E, B, E, W, E, S, S, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, W, W, W, E, E, W, W, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, B, E, E, E, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_two() -> List[List[str]]:
    """
    Level layout for level 2
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, P, E, W, E, W, E, S, S, W])
    grid.append([W, E, B, W, E, W, E, W, S, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, W, W, W, E, E, W, W, W])
    grid.append([W, E, B, E, W, E, E, E, E, W])
    grid.append([W, E, E, E, E, E, W, E, E, W])
    grid.append([W, E, W, E, B, W, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, S, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_three() -> List[List[str]]:
    """
    Level layout for level 3
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, P, E, E, W, W, E, E, S, W])
    grid.append([W, E, B, B, W, W, E, E, S, W])
    grid.append([W, E, B, E, W, E, E, E, E, W])
    grid.append([W, E, E, E, E, E, E, W, E, W])
    grid.append([W, E, B, W, E, W, E, E, E, W])
    grid.append([W, E, E, W, E, W, E, E, E, W])
    grid.append([W, E, E, E, E, W, E, E, E, W])
    grid.append([W, E, W, E, E, W, S, E, S, W])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_four() -> List[List[str]]:
    """
    Level layout for level 4
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, S, E, E, S, E, E, E, S, W])
    grid.append([W, E, E, E, S, E, E, E, E, W])
    grid.append([W, E, E, E, E, W, E, E, E, W])
    grid.append([W, E, W, B, B, B, E, E, E, W])
    grid.append([W, E, E, B, P, B, W, E, E, W])
    grid.append([W, E, W, B, B, B, E, E, E, W])
    grid.append([W, E, E, E, E, W, E, E, E, W])
    grid.append([W, S, E, E, S, E, E, E, S, W])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_five() -> List[List[str]]:
    """
    Level layout for level 5
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, P, W, E, E, E, E, E, E, W])
    grid.append([W, E, W, E, E, E, B, B, E, W])
    grid.append([W, E, W, E, E, W, W, E, E, W])
    grid.append([W, E, W, E, S, S, W, E, E, W])
    grid.append([W, E, W, S, S, S, W, E, E, W])
    grid.append([W, E, W, W, W, W, W, B, E, W])
    grid.append([W, E, B, E, B, E, E, E, E, W])
    grid.append([W, E, E, E, E, E, E, E, E, W])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_six() -> List[List[str]]:
    """
    Level layout for level 6
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, P, E, E, E, W, E, S, S, W])
    grid.append([W, E, E, B, E, W, E, S, S, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, W, W, W, E, E, W, W, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, B, E, E, E, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_seven() -> List[List[str]]:
    """
    Level layout for level 7
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, P, E, E, E, W, E, S, S, W])
    grid.append([W, E, E, B, E, W, E, S, S, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, W, W, W, E, E, W, W, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, B, E, E, E, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_eight() -> List[List[str]]:
    """
    Level layout for level 8
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, P, E, E, E, W, E, S, S, W])
    grid.append([W, E, E, B, E, W, E, S, S, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, W, W, W, E, E, W, W, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, B, E, E, E, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_nine() -> List[List[str]]:
    """
    Level layout for level 9
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, P, E, E, E, W, E, S, S, W])
    grid.append([W, E, E, B, E, W, E, S, S, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, W, W, W, E, E, W, W, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, B, E, E, E, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_ten() -> List[List[str]]:
    """
    level layout for level 10
    :return: Nested list consists of WALL, BOX, STORAGE, PLAYER, and EMPTY.
    """
    grid = List[List[str]]

    grid.append([W, W, W, W, W, W, W, W, W, W])
    grid.append([W, P, E, E, E, W, E, S, S, W])
    grid.append([W, E, E, B, E, W, E, S, S, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, W, W, W, E, E, W, W, W])
    grid.append([W, E, B, E, E, E, E, E, E, W])
    grid.append([W, E, B, E, E, E, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, E, E, E, E, W, W, E, E, W])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid

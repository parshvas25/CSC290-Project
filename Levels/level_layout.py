from typing import List, Tuple

"""
Wall layout for each level. Dimension is 6 by 6 (only considering the inner part
of the grid. Outermost layer should be walls and this setting is already covered 
in the different class.
"""

W = "wall"
B = "box"
P = "player"
S = "storage"
E = "empty"


def level_one() -> List:
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_two() -> List[Tuple[int]]:
    """
    Level layout for level 2
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_three() -> List[Tuple[int]]:
    """
    Level layout for level 3
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_four() -> List[Tuple[int]]:
    """
    Level layout for level 4
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_five() -> List[Tuple[int]]:
    """
    Level layout for level 5
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_six() -> List[Tuple[int]]:
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_seven() -> List[Tuple[int]]:
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_eight() -> List[Tuple[int]]:
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_nine() -> List[Tuple[int]]:
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid


def level_ten() -> List[Tuple[int]]:
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
    grid.append([W, E, E, E, E, W, W, E, E, E])
    grid.append([W, W, W, W, W, W, W, W, W, W])

    return grid

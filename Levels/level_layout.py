from typing import List, Tuple

"""
Wall layout for each level. Dimension is 6 by 6 (only considering the inner part
of the grid. Outermost layer should be walls and this setting is already covered 
in the different class.
"""


def level_one() -> List:
    """
    Wall layout for level 1.
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((2, 4))
    grid.append((3, 2))
    grid.append((4, 2))
    grid.append((5, 2))
    grid.append((5, 5))
    grid.append((5, 6))

    return grid


def level_two() -> List[Tuple[int]]:
    """
    Wall layout for level 2
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((2, 2))
    grid.append((2, 3))
    grid.append((2, 4))
    grid.append((2, 5))
    grid.append((3, 2))
    grid.append((4, 5))
    grid.append((5, 5))

    return grid


def level_three() -> List[Tuple[int]]:
    """
    Wall layout for level 3
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((4, 2))
    grid.append((4, 3))
    grid.append((4, 4))
    grid.append((4, 5))
    grid.append((3, 2))
    grid.append((3, 3))

    return grid


def level_four() -> List[Tuple[int]]:
    """
    Wall layout for level 4
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((3, 2))
    grid.append((3, 3))
    grid.append((3, 4))
    grid.append((3, 5))
    grid.append((2, 2))

    return grid


def level_five() -> List[Tuple[int]]:
    """
    Wall layout for level 5
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((2, 0))
    grid.append((2, 1))
    grid.append((2, 2))
    grid.append((2, 3))
    grid.append((3, 2))
    grid.append((4, 2))

    return grid


def level_six() -> List[Tuple[int]]:
    """
    Wall layout for level 6
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((2, 2))
    grid.append((2, 3))
    grid.append((2, 4))
    grid.append((2, 5))
    grid.append((5, 2))
    grid.append((5, 5))
    grid.append((5, 6))

    return grid


def level_seven() -> List[Tuple[int]]:
    """
    Wall layout for level 7
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((3, 2))
    grid.append((3, 3))
    grid.append((3, 4))
    grid.append((3, 5))
    grid.append((5, 2))
    grid.append((4, 2))

    return grid


def level_eight() -> List[Tuple[int]]:
    """
    Wall layout for level 8
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((1, 2))
    grid.append((1, 3))
    grid.append((1, 4))
    grid.append((2, 5))
    grid.append((3, 2))
    grid.append((4, 2))
    grid.append((5, 2))

    return grid


def level_nine() -> List[Tuple[int]]:
    """
    Wall layout for level 9
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((1, 2))
    grid.append((1, 3))
    grid.append((1, 4))
    grid.append((1, 5))
    grid.append((3, 2))
    grid.append((4, 2))
    grid.append((5, 2))

    return grid


def level_ten() -> List[Tuple[int]]:
    """
    Wall layout for level 10
    :return: Nested list consists of all coordinates of wall (inner part only)
    """
    grid = List[Tuple[int]]

    grid.append((2, 2))
    grid.append((2, 3))
    grid.append((2, 4))
    grid.append((2, 5))
    grid.append((3, 2))
    grid.append((4, 2))
    grid.append((5, 2))
    grid.append((5, 5))
    grid.append((5, 6))

    return grid

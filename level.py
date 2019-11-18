from typing import List

"""
Level layout for each level. Dimension is 10 by 10.
Outermost layer should be all walls. 
Each function will return a nested list consists of different types of objects
(e.g. wall, crate, player, storage, and empty grid).
"""

W = "wall"
C = "crate"
P = "player"
S = "storage"
E = "empty"


class Levels:
    """
    curr_level:
        Current level
    grid:
        Current level layout
    """
    curr_level: int
    grid: List[List[str]]

    def __init__(self, curr_level: int = 1) -> None:
        self.curr_level = curr_level
        self.grid = []
        getattr(Levels, "level_"+str(self.curr_level))(self)

    def advance(self):
        if self.curr_level <= 10:
            self.curr_level += 1
            self.grid = []
            getattr(Levels, "level_"+str(self.curr_level))(self)

    def level_1(self) -> None:
        """
        Level layout for level 1.
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, P, E, E, E, E, E, S, S, W])
        self.grid.append([W, E, E, C, E, E, E, S, S, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, W, W, W, E, E, W, W, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, C, E, E, E, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])

    def level_2(self) -> None:
        """
        Level layout for level 2
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, P, E, W, E, E, E, S, S, W])
        self.grid.append([W, E, C, W, E, E, E, W, S, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, W, W, W, E, E, W, W, W])
        self.grid.append([W, E, C, E, W, E, E, E, E, W])
        self.grid.append([W, E, E, E, E, E, W, E, E, W])
        self.grid.append([W, E, W, E, C, W, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, S, E])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])

    def level_3(self) -> None:
        """
        Level layout for level 3
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, P, E, E, W, W, E, E, S, W])
        self.grid.append([W, E, C, C, W, W, E, E, S, W])
        self.grid.append([W, E, C, E, W, E, E, E, E, W])
        self.grid.append([W, E, E, E, E, E, E, W, E, W])
        self.grid.append([W, E, C, W, E, W, E, E, E, W])
        self.grid.append([W, E, E, W, E, W, E, E, E, W])
        self.grid.append([W, E, E, E, E, W, E, E, E, W])
        self.grid.append([W, E, W, E, E, W, S, E, S, W])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])

    def level_4(self) -> None:
        """
        Level layout for level 4
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, S, E, E, S, E, E, E, S, W])
        self.grid.append([W, E, E, E, S, E, E, E, E, W])
        self.grid.append([W, E, E, E, E, W, E, E, E, W])
        self.grid.append([W, E, W, C, C, C, E, E, E, W])
        self.grid.append([W, E, E, C, P, C, W, E, E, W])
        self.grid.append([W, E, W, C, C, C, E, E, E, W])
        self.grid.append([W, E, E, E, E, W, E, E, E, W])
        self.grid.append([W, S, E, E, S, E, E, E, S, W])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])

    def level_5(self) -> None:
        """
        Level layout for level 5
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, P, W, E, E, E, E, E, E, W])
        self.grid.append([W, E, W, E, E, E, C, C, E, W])
        self.grid.append([W, E, W, E, E, W, W, E, E, W])
        self.grid.append([W, E, W, E, S, S, W, E, E, W])
        self.grid.append([W, E, W, S, S, S, W, E, E, W])
        self.grid.append([W, E, W, W, W, W, W, C, E, W])
        self.grid.append([W, E, C, E, C, E, E, E, E, W])
        self.grid.append([W, E, E, E, E, E, E, E, E, E])
        self.grid.append([W, E, W, W, W, W, W, C, E, W])
        self.grid.append([W, E, C, E, C, E, E, E, E, W])
        self.grid.append([W, E, E, E, E, E, E, E, E, W])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])

    def level_6(self) -> None:
        """
        Level layout for level 6
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, P, E, E, E, W, E, S, S, W])
        self.grid.append([W, E, E, C, E, W, E, S, S, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, W, W, W, E, E, W, W, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, C, E, E, E, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])

    def level_7(self) -> None:
        """
        Level layout for level 7
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, P, E, E, E, W, E, S, S, W])
        self.grid.append([W, E, E, C, E, W, E, S, S, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, W, W, W, E, E, W, W, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, C, E, E, E, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])

    def level_8(self) -> None:
        """
        Level layout for level 8
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, P, E, E, E, W, E, S, S, W])
        self.grid.append([W, E, E, C, E, W, E, S, S, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, W, W, W, E, E, W, W, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, C, E, E, E, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])

    def level_9(self) -> None:
        """
        Level layout for level 9
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, P, E, E, E, W, E, S, S, W])
        self.grid.append([W, E, E, C, E, W, E, S, S, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, W, W, W, E, E, W, W, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, C, E, E, E, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])

    def level_10(self) -> None:
        """
        level layout for level 10
        :return: Nested list consists of WALL, CRATE, STORAGE, PLAYER, and EMPTY.
        """
        self.grid.append([W, W, W, W, W, W, W, W, W, W])
        self.grid.append([W, P, E, E, E, W, E, S, S, W])
        self.grid.append([W, E, E, C, E, W, E, S, S, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, W, W, W, E, E, W, W, W])
        self.grid.append([W, E, C, E, E, E, E, E, E, W])
        self.grid.append([W, E, C, E, E, E, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, E, E, E, E, W, W, E, E, W])
        self.grid.append([W, W, W, W, W, W, W, W, W, W])



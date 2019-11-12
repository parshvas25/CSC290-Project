from typing import List


class Levels:
    """
    An abstract class to generate levels using grid system
    === Public Attributes ===
    EMPTY:
        An int to represent the grid at that point is empty
    WALL:
        An int to represent the grid at that point is a wall
    BOX:
        An int to represent the grid at that point is a box
    POINT:
        An int to represent the grid at that point is a point
    PLAYER:
        An int to represent the grid at that point is the player
    grid:
        A 2D list to represent each location
    """
    EMPTY: int
    WALL: int
    BOX: int
    POINT: int
    PLAYER: int
    grid: List[List[int]]

    def __init__(self) -> None:
        """
        Initialize a grid system for the game and all the variables
        """
        self.EMPTY, self.WALL, self.BOX, self.POINT, self.PLAYER = 0, 1, 2, 3, 4
        self.grid = []
        for i in range(10):
            self.grid.append([])
            for j in range(10):
                self.grid[i].extend([self.EMPTY])

    def _generate_level(self):
        """
        Generate a layout for the level (different levels have different
        layouts)
        """
        raise NotImplementedError


class LevelOne(Levels):

    def __init__(self):
        """
        Initialize the variables and generate the level
        """
        Levels.__init__(self)
        self._generate_level()

    def _generate_level(self):
        """
        Generate the level layout
        """
        for i in range(7):
            self.grid[0][i] = self.WALL
            self.grid[6][i] = self.WALL

        for i in range(7):
            self.grid[i][0] = self.WALL
            self.grid[i][7] = self.WALL
        self.grid[1][1] = self.PLAYER
        self.grid[2][3] = self.grid[3][2] = self.grid[2][5] = self.grid[5][2] \
            = self.BOX
        self.grid[1][6] = self.grid[2][6] = self.grid[5][6] = self.grid[5][4] \
            = self.POINT

from typing import List


class Levels:
    """
    An abstract class to generate levels using grid system
    === Public Attributes ===
    EMPTY:
        An str to represent the grid at that point is empty
    WALL:
        An str to represent the grid at that point is a wall
    CRATE:
        An str to represent the grid at that point is a crate
    STORAGE:
        An str to represent the grid at that point is a storage
    PLAYER:
        An str to represent the grid at that point is the player
    DONE:
        An str to represent a crate has been pushed into a storage
    level_list:
        A list that stores all the levels
    completed_level:
        A boolean for whether this level has been completed
    curr_level:
        Current level
    grid:
        A 2D list to represent location of each object
    """
    EMPTY: str
    WALL: str
    CRATE: str
    STORAGE: str
    PLAYER: str
    level_list: List
    completed_level: bool
    curr_level: str  # Unknown type yet
    grid: List[List[str]]

    def __init__(self) -> None:
        """
        Initialize a grid system for the game and all the variables
        """
        self.EMPTY, self.WALL, self.CRATE, self.STORAGE, self.PLAYER, \
            self.DONE = "", "W", "C", "S", "P", "D"
        self.grid = []
        for i in range(10):
            self.grid.append([])
            for j in range(10):
                self.grid[i].extend([self.EMPTY])

    def update_level_status(self):
        """
        Check if all the crates are pushed into the storage and update
        completed_level accordingly. Update current level if level completed.
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == self.STORAGE or self.grid[i][j] == \
                        self.CRATE:
                    self.completed_level = False
                    return None
        self.completed_level = True
        self.update_curr_level()

    def is_level_complete(self):
        """
        :return: the level status (completed or not)
        """
        self.update_level_status()
        return self.completed_level

    def is_game_complete(self):
        """
        Check if all the levels are completed
        :return: True if all levels are completed, False otherwise
        """
        for level in self.level_list:
            if not level.completed_level:
                return False
        return True

    def add_levels(self, level):
        """
        Add the :param level to the level list
        :param level: a level
        """
        self.level_list.append(level)

    def update_curr_level(self):
        """
        Update the current level to the next level
        """
        if self.is_game_complete():
            self.curr_level = None
            return None
        for level in self.level_list:
            if not level.is_level_complete():
                self.curr_level = level

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
            = self.CRATE
        self.grid[1][6] = self.grid[2][6] = self.grid[5][6] = self.grid[5][4] \
            = self.STORAGE

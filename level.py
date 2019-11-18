from level_layout import *


class Levels:
    """
    An abstract class to generate levels using grid system
    === Public Attributes ===
    E:
        An str to represent the grid at that point is empty
    W:
        An str to represent the grid at that point is a wall
    C:
        An str to represent the grid at that point is a crate
    S:
        An str to represent the grid at that point is a storage
    P:
        An str to represent the grid at that point is the player
    level_list:
        A list that stores all the layout of all levels
    completed_level:
        A boolean for whether this level has been completed
    curr_level:
        Current level
    """
    E: str
    W: str
    C: str
    S: str
    P: str
    level_list: List[List[List[str]]]
    completed_level: bool
    curr_level: str  # Unknown type yet

    def __init__(self) -> None:
        """
        Initialize a grid system for the game and all the variables
        """
        self.E, self.W, self.C, self.S, self.P = "", "wall", "crate", \
                                                 "storage", "player"
        self.level_list = []
        for i in range(1, 11):
            self.level_list.append(globals()['level_' + str(i)]())

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

    def is_complete(self):
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

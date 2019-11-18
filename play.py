import level
from level import *
from game_objects import *

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
MOVE_DISTANCE = 50


class Sokoban:

    def set_game_object(self, levels: Levels):
        Sokoban.wall_list = pygame.sprite.Group()
        Sokoban.crate_list = pygame.sprite.Group()
        Sokoban.storage_list = pygame.sprite.Group()
        Sokoban.player_group = pygame.sprite.Group()
        Sokoban.player = Player(0, 0)

        layout = levels.grid

        for i in range(len(layout)):
            for j in range(len(layout)):
                if layout[j][i] == level.W:
                    Sokoban.wall_list.add(Wall(i * 50, j * 50))
                elif layout[j][i] == level.C:
                    Sokoban.crate_list.add(Crate(i * 50, j * 50))
                elif layout[j][i] == level.S:
                    Sokoban.storage_list.add(Storage(i * 50, j * 50))
                elif layout[j][i] == level.P:
                    Sokoban.player = Player(i * 50, j * 50)
                    Sokoban.player_group.add(Sokoban.player)

    def play(self, curr_level: int = 1) -> None:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sokoban")

        levels = Levels(curr_level)
        self.set_game_object(levels)

        game_running = True
        is_moving = False
        clock = pygame.time.Clock()

        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                elif event.type == pygame.KEYDOWN:
                    if not is_moving:
                        is_moving = True
                        if event.key == pygame.K_LEFT:
                            Sokoban.player.move(-MOVE_DISTANCE, 0)
                        elif event.key == pygame.K_RIGHT:
                            Sokoban.player.move(MOVE_DISTANCE, 0)
                        elif event.key == pygame.K_UP:
                            Sokoban.player.move(0, -MOVE_DISTANCE)
                        elif event.key == pygame.K_DOWN:
                            Sokoban.player.move(0, MOVE_DISTANCE)
                        elif event.key == pygame.K_SPACE:
                            self.set_game_object(levels)

            screen.fill((192,192,192))
            Sokoban.player.update(Sokoban.wall_list, Sokoban.crate_list, Sokoban.storage_list)

            Sokoban.storage_list.draw(screen)

            Sokoban.player_group.draw(screen)
            Sokoban.wall_list.draw(screen)
            Sokoban.crate_list.draw(screen)

            if all([crate.stored for crate in Sokoban.crate_list]):
                levels.advance()
                self.set_game_object(levels)

            pygame.display.flip()  # End draw

            if is_moving:
                pygame.time.delay(100)
                is_moving = False


if __name__ == '__main__':
    sokoban = Sokoban()
    sokoban.play()

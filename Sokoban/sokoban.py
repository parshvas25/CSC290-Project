import level
import main_menu
import os
from game_objects import *
from level import *
from main_menu import *

# Global constants

# Colors
GAME_BACKGROUND = (192,192,192)

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
            for j in range(len(layout[i])):
                if layout[i][j] == level.W:
                    Sokoban.wall_list.add(Wall(j * 50, i * 50))
                elif layout[i][j] == level.C:
                    Sokoban.crate_list.add(Crate(j * 50, i * 50))
                elif layout[i][j] == level.S:
                    Sokoban.storage_list.add(Storage(j * 50, i * 50))
                elif layout[i][j] == level.P:
                    Sokoban.player = Player(j * 50, i * 50)
                    Sokoban.player_group.add(Sokoban.player)

    def play(self, curr_level):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sokoban")

        if curr_level is None:
            return

        levels = Levels(curr_level)
        self.set_game_object(levels)

        cur_path = os.path.dirname(__file__)
        new_path = os.path.relpath('..\\Resources\\Sounds', cur_path)
        pygame.mixer.init()
        pygame.mixer.music.load(new_path + "\\" + 'map_move.mp3')
        pygame.mixer.music.play(-1)

        move_sound = pygame.mixer.Sound(new_path + "\\" + 'walk_sound.wav')
        restart_level = pygame.mixer.Sound(
            new_path + "\\" + 'Electronic_Chime-495939803.wav')

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
                            move_sound.play()
                        elif event.key == pygame.K_RIGHT:
                            Sokoban.player.move(MOVE_DISTANCE, 0)
                            move_sound.play()
                        elif event.key == pygame.K_UP:
                            Sokoban.player.move(0, -MOVE_DISTANCE)
                            move_sound.play()
                        elif event.key == pygame.K_DOWN:
                            Sokoban.player.move(0, MOVE_DISTANCE)
                            move_sound.play()
                        elif event.key == pygame.K_SPACE:
                            self.set_game_object(levels)
                        elif event.key == pygame.K_ESCAPE:
                            curr_level = main_menu.main()
                            self.play(curr_level)
                            return
            screen.fill(GAME_BACKGROUND)
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

    start_level = main_menu.main()
    sokoban.play(start_level)

from level import *
from game_objects import *

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
MOVE_DISTANCE = 50


def get_game_object(level: Levels, level_num: int) -> List:
    wall_list = pygame.sprite.Group()
    crate_list = pygame.sprite.Group()
    storage_list = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    layout = level.level_list[level_num]

    for i in range(len(layout)):
        for j in range(len(layout)):

            if layout[j][i] == level.W:
                wall_list.add(Wall(i * 50, j * 50))
            elif layout[j][i] == level.C:
                crate_list.add(Crate(i * 50, j * 50))
            if layout[j][i] == level.S:
                storage_list.add(Storage(i * 50, j * 50))
            elif layout[j][i] == level.P:
                player = Player(i * 50, j * 50)
                player_group.add(player)

    return [wall_list, crate_list, storage_list, player_group, player]


def play() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sokoban")

    curr_level = 0
    level = Levels()

    wall_list, crate_list, storage_list, player_group, player = \
        get_game_object(level, curr_level)

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
                        player.move(-MOVE_DISTANCE, 0)
                    elif event.key == pygame.K_RIGHT:
                        player.move(MOVE_DISTANCE, 0)
                    elif event.key == pygame.K_UP:
                        player.move(0, -MOVE_DISTANCE)
                    elif event.key == pygame.K_DOWN:
                        player.move(0, MOVE_DISTANCE)
                    elif event.key == pygame.K_SPACE:
                        wall_list, crate_list, storage_list, player_group, \
                        player = get_game_object(level, 0)

        screen.fill(BLACK)
        player.update(wall_list, crate_list, storage_list)

        storage_list.draw(screen)

        player_group.draw(screen)
        wall_list.draw(screen)
        crate_list.draw(screen)

        if all([crate.stored for crate in crate_list]) and curr_level < 10:
            curr_level += 1
            wall_list, crate_list, storage_list, player_group, player = \
                get_game_object(level, curr_level)

        pygame.display.flip()  # End draw

        if is_moving:
            pygame.time.delay(100)
            is_moving = False


if __name__ == '__main__':
    play()

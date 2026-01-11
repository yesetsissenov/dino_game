import sys

import pygame

from game import config
from game.entities import Dino, ObstacleManager
from game.ui import Scoreboard
from game.world import World


def handle_events(dino: Dino, game_over: bool) -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                if game_over:
                    return True
                dino.jump()
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Dino Runner")
    clock = pygame.time.Clock()

    dino = Dino(x=config.DINO_START_X, y=config.DINO_START_Y)
    obstacles = ObstacleManager()
    world = World()
    scoreboard = Scoreboard()

    running = True
    game_over = False

    while running:
        delta_ms = clock.tick(config.FPS)
        if not handle_events(dino, game_over):
            running = False
            continue

        if not game_over:
            dino.update()
            world.update(delta_ms)
            obstacles.update(world.speed)
            if obstacles.collides(dino.rect):
                game_over = True
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                dino = Dino(x=config.DINO_START_X, y=config.DINO_START_Y)
                obstacles = ObstacleManager()
                world.reset()
                game_over = False

        screen.fill(world.background_color())
        foreground = world.foreground_color()
        world.draw_ground(screen, foreground)
        obstacles.draw(screen, foreground)
        dino.draw(screen, foreground)
        scoreboard.draw(screen, foreground, world.score, world.high_score)

        if game_over:
            scoreboard.draw_message(screen, foreground, "Game Over - Press Space")

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

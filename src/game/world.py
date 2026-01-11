import pygame

from . import config


class World:
    def __init__(self) -> None:
        self.score = 0.0
        self.high_score = 0.0
        self.daytime = True
        self.cycle_timer = 0
        self.speed = config.OBSTACLE_SPEED_START

    def update(self, delta_ms: int) -> None:
        self.score += config.SCORE_INCREMENT
        self.high_score = max(self.high_score, self.score)
        self.speed = min(config.OBSTACLE_SPEED_MAX, self.speed + config.OBSTACLE_SPEED_INCREMENT * delta_ms)
        self.cycle_timer += delta_ms
        if self.cycle_timer >= config.DAY_NIGHT_CYCLE_MS:
            self.daytime = not self.daytime
            self.cycle_timer = 0

    def reset(self) -> None:
        self.score = 0.0
        self.speed = config.OBSTACLE_SPEED_START
        self.cycle_timer = 0
        self.daytime = True

    def background_color(self) -> tuple[int, int, int]:
        return config.DAY_COLOR if self.daytime else config.NIGHT_COLOR

    def foreground_color(self) -> tuple[int, int, int]:
        return config.FOREGROUND_DAY if self.daytime else config.FOREGROUND_NIGHT

    def draw_ground(self, surface: pygame.Surface, color: tuple[int, int, int]) -> None:
        pygame.draw.line(
            surface,
            color,
            (0, config.GROUND_Y),
            (config.SCREEN_WIDTH, config.GROUND_Y),
            2,
        )

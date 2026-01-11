from dataclasses import dataclass
import random

import pygame

from . import config


@dataclass
class Dino:
    x: float
    y: float
    velocity_y: float = 0
    is_jumping: bool = False
    leg_frame: int = 0

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y - config.DINO_HEIGHT, config.DINO_WIDTH, config.DINO_HEIGHT)

    def jump(self) -> None:
        if not self.is_jumping:
            self.velocity_y = config.DINO_JUMP_VELOCITY
            self.is_jumping = True

    def update(self) -> None:
        if self.is_jumping:
            self.velocity_y += config.DINO_GRAVITY
            self.y += self.velocity_y
            if self.y >= config.DINO_START_Y:
                self.y = config.DINO_START_Y
                self.velocity_y = 0
                self.is_jumping = False
        self.leg_frame = (self.leg_frame + 1) % 20

    def draw(self, surface: pygame.Surface, color: tuple[int, int, int]) -> None:
        body_rect = self.rect
        pygame.draw.rect(surface, color, body_rect)
        eye_rect = pygame.Rect(body_rect.x + 26, body_rect.y + 10, 4, 4)
        pygame.draw.rect(surface, surface.get_colorkey() or (0, 0, 0), eye_rect)
        leg_height = 8 if self.leg_frame < 10 else 4
        leg_rect = pygame.Rect(body_rect.x + 6, body_rect.y + body_rect.height - leg_height, 8, leg_height)
        pygame.draw.rect(surface, color, leg_rect)


@dataclass
class Obstacle:
    x: float
    y: float
    width: int
    height: int
    kind: str

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y - self.height, self.width, self.height)

    def update(self, speed: float) -> None:
        self.x -= speed

    def draw(self, surface: pygame.Surface, color: tuple[int, int, int]) -> None:
        if self.kind == "cactus":
            self._draw_cactus(surface, color)
        else:
            self._draw_ptero(surface, color)

    def _draw_cactus(self, surface: pygame.Surface, color: tuple[int, int, int]) -> None:
        rect = self.rect
        pygame.draw.rect(surface, color, rect)
        arm_width = max(6, rect.width // 3)
        arm_height = rect.height // 3
        left_arm = pygame.Rect(rect.x - arm_width, rect.y + arm_height, arm_width, arm_height)
        right_arm = pygame.Rect(rect.x + rect.width, rect.y + arm_height // 2, arm_width, arm_height)
        pygame.draw.rect(surface, color, left_arm)
        pygame.draw.rect(surface, color, right_arm)

    def _draw_ptero(self, surface: pygame.Surface, color: tuple[int, int, int]) -> None:
        rect = self.rect
        body = pygame.Rect(rect.x + 10, rect.y + 8, rect.width - 20, rect.height - 12)
        pygame.draw.rect(surface, color, body)
        wing_span = rect.width // 2
        left_wing = pygame.Rect(rect.x, rect.y + 4, wing_span, 6)
        right_wing = pygame.Rect(rect.x + wing_span, rect.y + 4, wing_span, 6)
        pygame.draw.rect(surface, color, left_wing)
        pygame.draw.rect(surface, color, right_wing)


class ObstacleManager:
    def __init__(self) -> None:
        self.obstacles: list[Obstacle] = []
        self.distance_until_next = random.randint(config.OBSTACLE_MIN_GAP, config.OBSTACLE_MAX_GAP)

    def update(self, speed: float) -> None:
        self.distance_until_next -= speed
        if self.distance_until_next <= 0:
            self.spawn_obstacle()
            self.distance_until_next = random.randint(config.OBSTACLE_MIN_GAP, config.OBSTACLE_MAX_GAP)
        for obstacle in self.obstacles:
            obstacle.update(speed)
        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.x + obstacle.width > 0]

    def spawn_obstacle(self) -> None:
        if random.random() < config.PTERO_SPAWN_CHANCE:
            height = random.randint(config.PTERO_MIN_HEIGHT, config.PTERO_MAX_HEIGHT)
            obstacle = Obstacle(
                x=config.SCREEN_WIDTH + config.PTERO_WIDTH,
                y=height,
                width=config.PTERO_WIDTH,
                height=config.PTERO_HEIGHT,
                kind="ptero",
            )
        else:
            size_index = random.randint(0, len(config.CACTUS_WIDTHS) - 1)
            width = config.CACTUS_WIDTHS[size_index]
            height = config.CACTUS_HEIGHTS[size_index]
            obstacle = Obstacle(
                x=config.SCREEN_WIDTH + width,
                y=config.GROUND_Y,
                width=width,
                height=height,
                kind="cactus",
            )
        self.obstacles.append(obstacle)

    def draw(self, surface: pygame.Surface, color: tuple[int, int, int]) -> None:
        for obstacle in self.obstacles:
            obstacle.draw(surface, color)

    def collides(self, rect: pygame.Rect) -> bool:
        return any(obstacle.rect.colliderect(rect) for obstacle in self.obstacles)

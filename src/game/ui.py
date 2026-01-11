import pygame

from . import config


class Scoreboard:
    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Courier", 18, bold=True)

    def draw(self, surface: pygame.Surface, color: tuple[int, int, int], score: float, high_score: float) -> None:
        score_text = f"{int(score):05d}"
        high_text = f"HI {int(high_score):05d}"
        score_render = self.font.render(score_text, True, color)
        high_render = self.font.render(high_text, True, color)
        surface.blit(high_render, (config.SCREEN_WIDTH - 180, 20))
        surface.blit(score_render, (config.SCREEN_WIDTH - 90, 20))

    def draw_message(self, surface: pygame.Surface, color: tuple[int, int, int], message: str) -> None:
        text = self.font.render(message, True, color)
        rect = text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        surface.blit(text, rect)

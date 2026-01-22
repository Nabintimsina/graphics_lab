import sys
import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    game = Game(screen)
    game.run()

    sys.exit()


if __name__ == "__main__":
    main()
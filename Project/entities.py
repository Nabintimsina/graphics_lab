import pygame
import random
from settings import *


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
        self.image.fill(COLOR_BIRD)
        self.rect = self.image.get_rect()
        self.rect.center = (BIRD_START_X, BIRD_START_Y)
        self.velocity = 0


    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def jump(self):
        self.velocity = JUMP_STRENGTH


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, is_top):
        super().__init__()
        self.image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.image.fill(COLOR_PIPE)
        self.rect = self.image.get_rect()
        if is_top:
            self.rect.bottomleft = (x, y - PIPE_GAP // 2)
        else:
            self.rect.topleft = (x, y + PIPE_GAP // 2)


    def update(self):
        self.rect.x -= PIPE_SPEED

import sys
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLOR_BG
from entities import Bird, Pipe

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

bird = Bird()

all_sprites = pygame.sprite.Group()
all_sprites.add(bird)

pipe_group = pygame.sprite.Group()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()


        screen.fill(COLOR_BG) 
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

   

if __name__ == "__main__":
    main()
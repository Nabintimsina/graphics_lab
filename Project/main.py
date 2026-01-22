import sys
import pygame
# from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLOR_BG
from settings import *

from entities import Bird, Pipe

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

bird = Bird()

all_sprites = pygame.sprite.Group()
all_sprites.add(bird)

pipe_group = pygame.sprite.Group()
pipe_x = SCREEN_WIDTH + 100  # start a bit off-screen to the right
pipe_y = SCREEN_HEIGHT // 2   # middle of the screen for now
top_pipe_y = pipe_y - PIPE_GAP // 2 
bottom_pipe_y = pipe_y + PIPE_GAP // 2


top_pipe = Pipe(pipe_x, top_pipe_y, is_top=True)
bottom_pipe = Pipe(pipe_x, bottom_pipe_y, is_top=False)
pipe_group.add(top_pipe, bottom_pipe)
all_sprites.add(top_pipe, bottom_pipe)


def main():

    game_state = "start"  # can be "start", "playing", "game_over"


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state == "start":
                        game_state = "playing"
                        bird.jump()  # optional: first jump immediately
                    elif game_state == "playing":
                        bird.jump()
                    elif game_state == "game_over":
                        # restart the game (we'll define a reset later)
                        # e.g. call a function reset_game()
                        pass


        screen.fill(COLOR_BG) 

        if game_state == "playing":
            all_sprites.update()

            for pipe in list(pipe_group):
                if pipe.rect.right < 0:
                    pipe.kill()  # removes it from all groups

            pipe_collisions = pygame.sprite.spritecollide(bird, pipe_group, False)
            if pipe_collisions:
                game_state = "game_over"
            if bird.rect.bottom >= SCREEN_HEIGHT:
                game_state = "game_over"
            if bird.rect.top <= 0:
                game_state = "game_over"
            

        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

   

if __name__ == "__main__":
    main()
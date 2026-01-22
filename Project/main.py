import sys
import pygame
import random
from settings import *

from entities import Bird, Pipe

pygame.init()

font = pygame.font.Font(None, 48)  # default font, size 48


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

bird = Bird()

all_sprites = pygame.sprite.Group()
all_sprites.add(bird)
pipe_group = pygame.sprite.Group()




game_state = "start"  # can be "start", "playing", "game_over"
pipe_spawn_counter = 0  # counts frames since last spawn
score = 0
pipe_pairs = []  # holds dicts like {"x": center_x, "passed": False}
running = True





def spawn_pipe_pair(pipe_group, all_sprites , pipe_pairs):
    pipe_x = SCREEN_WIDTH 

    min_pipe_y = 100
    max_pipe_y = SCREEN_HEIGHT - 100
    pipe_y = random.randint(min_pipe_y, max_pipe_y)

    top_pipe_y = pipe_y - PIPE_GAP // 2 - PIPE_HEIGHT
    bottom_pipe_y = pipe_y + PIPE_GAP // 2

    top_pipe = Pipe(pipe_x, top_pipe_y, is_top=True)
    bottom_pipe = Pipe(pipe_x, bottom_pipe_y, is_top=False)

    pipe_group.add(top_pipe, bottom_pipe)
    all_sprites.add(top_pipe, bottom_pipe)

    pipe_pairs.append({"pipe": bottom_pipe, "passed": False})
    
 


def reset_game(bird, pipe_group, all_sprites, pipe_pairs):
    global game_state, score, pipe_spawn_counter

    # reset bird
    bird.rect.center = (BIRD_START_X, BIRD_START_Y)
    bird.velocity = 0

    # remove all pipes
    for pipe in list(pipe_group):
        pipe.kill()  # removes from both groups

    # clear pipe_pairs list
    pipe_pairs.clear()

    # reset score and counter
    score = 0
    pipe_spawn_counter = 0

    # go back to start state
    game_state = "start"









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
                    reset_game(bird, pipe_group, all_sprites, pipe_pairs)



    if game_state == "playing":
        all_sprites.update()

        pipe_collisions = pygame.sprite.spritecollide(bird, pipe_group, False)
        if pipe_collisions:
            game_state = "game_over"
        if bird.rect.bottom >= SCREEN_HEIGHT:
            game_state = "game_over"
        if bird.rect.top <= 0:
            game_state = "game_over"

        pipe_spawn_counter += 1
        if pipe_spawn_counter >= PIPE_SPAWN_INTERVAL:
            pipe_spawn_counter = 0
            spawn_pipe_pair(pipe_group, all_sprites, pipe_pairs)

        for pair in pipe_pairs:
            pipe = pair["pipe"]
            if(not pair["passed"] and pipe.rect.centerx < bird.rect.centerx):

                pair["passed"] = True
                score += 1

        for pipe in list(pipe_group):
            if pipe.rect.right < 0:
                pipe.kill()  # removes it from all groups
                pipe_pairs[:] = [pair for pair in pipe_pairs if pair["pipe"].alive()]



 
    screen.fill(COLOR_BG) 
    all_sprites.draw(screen)


    score_text = str(score)
    score_surf = font.render(score_text, True, COLOR_TEXT)  # white
    score_rect = score_surf.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(score_surf, score_rect)


    if game_state == "start":
        msg = "Press SPACE to start"
    elif game_state == "game_over":
        msg = "Game Over! "
    else:
        msg = None

    if msg:
        msg_surf = font.render(msg, True, COLOR_TEXT)
        msg_rect = msg_surf.get_rect(center=(SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 -100))
        screen.blit(msg_surf, msg_rect)


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()

   


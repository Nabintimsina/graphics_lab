import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumping Dino with Image")
clock = pygame.time.Clock()

# Load Dino Image
dino_image = pygame.image.load('project2/dino.png')  # Replace with your dino image file
dino_width, dino_height = 50, 50  # Resize to desired dimensions
dino_image = pygame.transform.scale(dino_image, (dino_width, dino_height))

# Dino properties
dino_x = 50
dino_y = SCREEN_HEIGHT - dino_height - 20
dino_velocity_y = 0
gravity = 1.5
jump_power = -20
is_jumping = False

# Obstacle (Cactus) properties
cactus_width = 20
cactus_height = 30
cactus_x = SCREEN_WIDTH
cactus_y = SCREEN_HEIGHT - cactus_height - 20
cactus_speed = 10

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop condition
running = True

while running:
    screen.fill(WHITE)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                dino_velocity_y = jump_power
                is_jumping = True

    # Dino gravity and jumping mechanics
    dino_velocity_y += gravity
    dino_y += dino_velocity_y
    if dino_y >= SCREEN_HEIGHT - dino_height - 20:
        dino_y = SCREEN_HEIGHT - dino_height - 20
        is_jumping = False

    # Move the cactus
    cactus_x -= cactus_speed
    if cactus_x < -cactus_width:
        cactus_x = SCREEN_WIDTH
        cactus_height = random.randint(20, 50)
        cactus_y = SCREEN_HEIGHT - cactus_height - 20
        score += 1
        cactus_speed += 0.5  # Increase speed for added difficulty

    # Check for collision
    if (dino_x + dino_width > cactus_x and
        dino_x < cactus_x + cactus_width and
        dino_y + dino_height > cactus_y):
        # Game over screen
        game_over_text = font.render("Game Over! Score: " + str(score), True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Draw dino (using image)
    screen.blit(dino_image, (dino_x, dino_y))

    # Draw cactus
    pygame.draw.rect(screen, BLACK, (cactus_x, cactus_y, cactus_width, cactus_height))

    # Display score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
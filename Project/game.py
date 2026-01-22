import pygame
import random

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    COLOR_BG,
    COLOR_TEXT,
    COLOR_GROUND,
    GROUND_Y,
    GROUND_HEIGHT,
    PIPE_GAP,
    PIPE_HEIGHT,
    PIPE_SPAWN_INTERVAL,
    BIRD_START_X,
    BIRD_START_Y,
)

from entities import Bird, Pipe


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.clock = pygame.time.Clock()

        # Fonts
        self.font = pygame.font.Font(None, 30)

        # Entities and groups
        self.bird = Bird()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bird)

        self.pipe_group = pygame.sprite.Group()

        # Ground
        self.ground_rect = pygame.Rect(0, GROUND_Y, SCREEN_WIDTH, GROUND_HEIGHT)

        # Game state
        self.game_state = "start"  # "start", "playing", "game_over"
        self.pipe_spawn_counter = 0  # frames since last spawn
        self.score = 0
        # Each entry: {"pipe": bottom_pipe_sprite, "passed": bool}
        self.pipe_pairs = []

        self.running = True

    # ---------- Game setup / reset ----------

    def spawn_pipe_pair(self) :
        """Create a top and bottom pipe with a random vertical gap."""
        pipe_x = SCREEN_WIDTH

        min_pipe_y = 100
        max_pipe_y = SCREEN_HEIGHT - 100
        pipe_y = random.randint(min_pipe_y, max_pipe_y)

        top_pipe_y = pipe_y - PIPE_GAP // 2 
        bottom_pipe_y = pipe_y + PIPE_GAP // 2

        top_pipe = Pipe(pipe_x, top_pipe_y, is_top=True)
        bottom_pipe = Pipe(pipe_x, bottom_pipe_y, is_top=False)

        self.pipe_group.add(top_pipe, bottom_pipe)
        self.all_sprites.add(top_pipe, bottom_pipe)

        # Track the bottom pipe for scoring
        self.pipe_pairs.append({"pipe": bottom_pipe, "passed": False})

    def reset_game(self):
        """Reset bird, pipes, score, and timers after game over."""
        # Reset bird
        self.bird.rect.center = (BIRD_START_X, BIRD_START_Y)
        self.bird.velocity = 0

        # Remove all pipes
        for pipe in list(self.pipe_group):
            pipe.kill()

        # Clear scoring info
        self.pipe_pairs.clear()

        # Reset counters and score
        self.score = 0
        self.pipe_spawn_counter = 0

        # Back to start state
        self.game_state = "start"

    # ---------- Main loop pieces ----------

    def handle_events(self) :
        """Handle input and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_state == "start":
                        self.game_state = "playing"
                        self.bird.jump()
                    elif self.game_state == "playing":
                        self.bird.jump()
                    elif self.game_state == "game_over":
                        self.reset_game()


    def update(self) :
        """Update game state for one frame."""
        if self.game_state == "playing":
            # Pipe spawn timer
            self.pipe_spawn_counter += 1
            if self.pipe_spawn_counter >= PIPE_SPAWN_INTERVAL:
                self.pipe_spawn_counter = 0
                self.spawn_pipe_pair()

            # Update bird and pipes
            self.all_sprites.update()

            # Collisions with pipes
            pipe_collisions = pygame.sprite.spritecollide(self.bird, self.pipe_group, False)
            if pipe_collisions:
                self.game_state = "game_over"

            # Collisions with ground and top of screen
            if self.bird.rect.bottom >= self.ground_rect.top:
                self.game_state = "game_over"
            if self.bird.rect.top <= 0:
                self.game_state = "game_over"

            # Scoring: when a pipe passes behind the bird
            for pair in self.pipe_pairs:
                pipe = pair["pipe"]
                if (not pair["passed"]
                        and pipe.rect.centerx < self.bird.rect.centerx):
                    pair["passed"] = True
                    self.score += 1

            # Remove off-screen pipes
            for pipe in list(self.pipe_group):
                if pipe.rect.right < 0:
                    pipe.kill()

            # Remove stale pipe_pairs entries
            self.pipe_pairs[:] = [
                pair for pair in self.pipe_pairs
                if pair["pipe"].alive()
            ]

        # Limit FPS
        self.clock.tick(FPS)

    def draw(self) :
        """Draw everything for one frame."""
        # Background
        self.screen.fill(COLOR_BG)

        # Sprites
        self.all_sprites.draw(self.screen)

        # Ground
        pygame.draw.rect(self.screen, COLOR_GROUND, self.ground_rect)

        # Score
        score_text = str(self.score)
        score_surf = self.font.render(score_text, True, COLOR_TEXT)
        score_rect = score_surf.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(score_surf, score_rect)

        # Messages
        if self.game_state == "start":
            msg = "Press SPACE to start"
        elif self.game_state == "game_over":
            msg = "Game Over! Press SPACE to restart"
        else:
            msg = None

        if msg:
            msg_surf = self.font.render(msg, True, COLOR_TEXT)
            msg_rect = msg_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
            self.screen.blit(msg_surf, msg_rect)

        pygame.display.update()


    def run(self) :
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 40  # For grid-based movement
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger Clone")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
TURQUOISE = (0,255,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
PINK = (255,192,203)
PURPLE = (128,0,128)
BROWN = (165,42,42)
BLACK = (0,0,0)
GRAY = (128,128,128)
DARK_GRAY = (169,169,169)
LIGHT_GRAY = (211,211,211)
GOLD = (255,215,0)
SILVER = (192,192,192)
BRONZE = (205,127,50)
MAROON = (128,0,0)
NAVY = (0,0,128)
OLIVE = (128,128,0)
TEAL = (0,128,128)
    


# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = GRID_SIZE

    def move(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= self.speed
        elif direction == "down" and self.y < HEIGHT - GRID_SIZE:
            self.y += self.speed
        elif direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < WIDTH - GRID_SIZE:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, GRID_SIZE, GRID_SIZE))

# Obstacle class
class Obstacle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = -GRID_SIZE  # Reset to left side
        elif self.x < -GRID_SIZE:
            self.x = WIDTH  # Reset to right side

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, GRID_SIZE, GRID_SIZE))

# Game setup
player = Player(WIDTH // 2, HEIGHT - GRID_SIZE)  # Start at bottom center
obstacles = [Obstacle(random.randint(0, WIDTH), i * GRID_SIZE, 2) for i in range(1, 5)]  # Some obstacles
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move("up")
            elif event.key == pygame.K_DOWN:
                player.move("down")
            elif event.key == pygame.K_LEFT:
                player.move("left")
            elif event.key == pygame.K_RIGHT:
                player.move("right")

    # Update obstacles
    for obstacle in obstacles:
        obstacle.move()

    # Collision detection
    for obstacle in obstacles:
        if (player.x == obstacle.x and player.y == obstacle.y):
            print("Collision! Game Over!")
            running = False

    # Draw everything
    screen.fill(WHITE)
    player.draw()
    for obstacle in obstacles:
        obstacle.draw()
    pygame.display.flip()

    clock.tick(60)  # 60 FPS

pygame.quit()
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger Game")

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

# Handler for the sprite sheet images
class SpriteSheet:
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height)).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image
    
# Load sprite sheet
sprite_sheet = SpriteSheet("cars.png")

# Load the start screen image
intro_image = pygame.image.load("Intro.png")
intro_image = pygame.transform.scale(intro_image, (WIDTH, HEIGHT))

# Font for start screen text
font = pygame.font.Font(None, 74)

#extract the sprite
SPRITE_WIDTH = 60
SPRITE_HEIGHT = 100

# Extract the car1 sprite from the sprite sheet
car1 = sprite_sheet.get_image(240, 20, SPRITE_WIDTH, SPRITE_HEIGHT)# First row, third column

# Scale the car sprite to fit the grid size
car1 = pygame.transform.scale(car1, (GRID_SIZE, GRID_SIZE))
#car1 = pygame.transform.rotate(car1, -90)  # Negative angle for clockwise rotation

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

# Obstacle class (now using car1 sprite)
class Obstacle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = car1  # Use the car1 sprite
        self.rect = self.image.get_rect(topleft=(x, y))  # Get the rectangle for positioning and collision

    def move(self):
        self.x += self.speed
        self.rect.x = self.x  # Update the rect position
        if self.x > WIDTH:
            self.x = -GRID_SIZE
            self.rect.x = self.x
        elif self.x < -GRID_SIZE:
            self.x = WIDTH
            self.rect.x = self.x

    def draw(self):
        screen.blit(self.image, (self.x, self.y))  # Draw the car sprite

# Game setup
player = Player(WIDTH // 2, HEIGHT - GRID_SIZE)
obstacles = [Obstacle(random.randint(0, WIDTH), i * GRID_SIZE, 2) for i in range(1, 5)]
clock = pygame.time.Clock()

# Game state
game_state = "start"

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == "start" and event.key == pygame.K_RETURN:
                game_state = "playing"
            elif game_state == "playing":
                if event.key == pygame.K_UP:
                    player.move("up")
                elif event.key == pygame.K_DOWN:
                    player.move("down")
                elif event.key == pygame.K_LEFT:
                    player.move("left")
                elif event.key == pygame.K_RIGHT:
                    player.move("right")

    # Handle game states
    if game_state == "start":
        screen.blit(intro_image, (0, 0))
        # Uncomment to add "Press Enter to Start" text if needed
        # text = font.render("Press Enter to Start", True, BLACK)
        # text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        # screen.blit(text, text_rect)

    elif game_state == "playing":
        for obstacle in obstacles:
            obstacle.move()

        # Collision detection using rects
        player_rect = pygame.Rect(player.x, player.y, GRID_SIZE, GRID_SIZE)
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle.rect):
                print("Collision! Game Over!")
                running = False

        screen.fill(WHITE)
        player.draw()
        for obstacle in obstacles:
            obstacle.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
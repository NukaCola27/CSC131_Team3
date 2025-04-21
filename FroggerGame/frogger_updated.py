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

# Frog
frog_image = pygame.image.load("frog.png").convert_alpha()
frog_image = pygame.transform.scale(frog_image, (GRID_SIZE, GRID_SIZE))  # Match size


# Font for start screen text
font = pygame.font.Font(None, 74)

# Extract the sprites
SPRITE_WIDTH = 40
SPRITE_HEIGHT = 100

# Extract the car sprites from the sprite sheet
car1 = sprite_sheet.get_image(250, 20, SPRITE_WIDTH, SPRITE_HEIGHT)  # First row, 5th car

car2 = sprite_sheet.get_image(190, 16, SPRITE_WIDTH, SPRITE_HEIGHT)  # First row, 4th car

car3 = sprite_sheet.get_image(130, 16, SPRITE_WIDTH, SPRITE_HEIGHT)  # First row, 3rd car

car4 = sprite_sheet.get_image(10, 440, SPRITE_WIDTH, SPRITE_HEIGHT)  # Fifth row, 1st car
car5 = sprite_sheet.get_image(74, 440, SPRITE_WIDTH, SPRITE_HEIGHT)  # Fifth row, 2nd car
car6 = sprite_sheet.get_image(137, 440, SPRITE_WIDTH, SPRITE_HEIGHT)  # Fifth row, 3rd car
car7 = sprite_sheet.get_image(200, 440, SPRITE_WIDTH, SPRITE_HEIGHT)  # Fifth row, 4th car

# Scale the car sprites to fit the grid size
#car1 = pygame.transform.scale(car1, (GRID_SIZE, GRID_SIZE))
#car2 = pygame.transform.scale(car2, (GRID_SIZE, GRID_SIZE))
#car3 = pygame.transform.scale(car3, (GRID_SIZE, GRID_SIZE))
#car4 = pygame.transform.scale(car4, (GRID_SIZE, GRID_SIZE))
#car5 = pygame.transform.scale(car5, (GRID_SIZE, GRID_SIZE))
#car6 = pygame.transform.scale(car6, (GRID_SIZE, GRID_SIZE))
#car7 = pygame.transform.scale(car7, (GRID_SIZE, GRID_SIZE))

# Rotate all car sprites 90 degrees to the right (clockwise)
car1 = pygame.transform.rotate(car1, -90)
car2 = pygame.transform.rotate(car2, -90)
car3 = pygame.transform.rotate(car3, -90)
car4 = pygame.transform.rotate(car4, -90)
car5 = pygame.transform.rotate(car5, -90)
car6 = pygame.transform.rotate(car6, -90)
car7 = pygame.transform.rotate(car7, -90)

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
        screen.blit(frog_image, (self.x, self.y))

# Obstacle class (accepting a specific sprite)
class Obstacle:
    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = sprite  # Use the specified sprite
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self):
        self.x += self.speed
        self.rect.x = self.x
        if self.x > WIDTH:
            self.x = -GRID_SIZE
            self.rect.x = self.x
        elif self.x < -GRID_SIZE:
            self.x = WIDTH
            self.rect.x = self.x

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Game setup
def initialize_game():
 player = Player(WIDTH // 2, HEIGHT - GRID_SIZE)
 obstacles = []
 # Row 1: y=40, car1, speed 2 (right)
 obstacles.extend([Obstacle(random.randint(0, WIDTH), 40, 2, car1) for _ in range(2)])
 # Row 2: y=80, car2, speed -3 (left)
 obstacles.extend([Obstacle(random.randint(0, WIDTH), 80, -3, car2) for _ in range(2)])

 # Row 3: y=120, car3, speed 4 (right)
 obstacles.extend([Obstacle(random.randint(0, WIDTH), 120, 4, car3) for _ in range(2)])
 # Row 4: y=160, car4, speed -2 (left)
 obstacles.extend([Obstacle(random.randint(0, WIDTH), 160, -2, car4) for _ in range(2)])
 # Row 5: y=200, car5, speed 3 (right)
 obstacles.extend([Obstacle(random.randint(0, WIDTH), 200, 3, car5) for _ in range(2)])
 # Row 6: y=240, car6, speed -4 (left)
 obstacles.extend([Obstacle(random.randint(0, WIDTH), 240, -4, car6) for _ in range(2)])
 # Row 7: y=280, car7, speed 2 (right)
 obstacles.extend([Obstacle(random.randint(0, WIDTH), 280, 2, car7) for _ in range(2)])
 # Row 8: y=320, car1, speed -3 (left)
 obstacles.extend([Obstacle(random.randint(0, WIDTH), 320, -3, car1) for _ in range(2)])

 # Row 9: y=360, car2, speed 1 (right)
 obstacles.extend([Obstacle(random.randint(0, WIDTH), 360, 1, car2) for _ in range(2)])
 return player, obstacles

#Game Setup 
player, obstacles = initialize_game()
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
            elif game_state in ("game_over", "victory") and event.key == pygame.K_RETURN:
                # Reset the game by reinitializing player and obstacles
                player, obstacles = initialize_game()
                game_state = "start"    

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
               # print("Collision! Game Over!")
                game_state = "game_over"
                break

        # ***** Added win condition check ******
        if player.y <= 0:
            game_state = "victory"  # player reaches the top

        if game_state == "playing":
            screen.fill(WHITE)

            # ***** Added lane background coloring for better visual distinction ******
            for i in range(10):
                color = DARK_GRAY if i % 2 == 0 else LIGHT_GRAY
                pygame.draw.rect(screen, color, (0, i * GRID_SIZE, WIDTH, GRID_SIZE))

            player.draw()
            for obstacle in obstacles:
                obstacle.draw()

    elif game_state == "game_over":
        screen.fill(BLACK)  # Black background for game over screen
        text = font.render("""Retry? Press enter to try again""", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    # ***** Added Victory Screen ******
    elif game_state == "victory":
        screen.fill(GREEN)
        text = font.render("You Win! Press Enter", True, WHITE)  # <<< shorter text
        text2 = font.render("to Play Again", True, WHITE)  # <<< second short line

        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))  # moved up a bit
        text2_rect = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))  # moved down a bit

        screen.blit(text, text_rect)
        screen.blit(text2, text2_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
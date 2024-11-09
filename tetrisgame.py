import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Define shapes of the Tetris blocks
shapes = [
    [[1, 1, 1, 1]],              # I
    [[1, 1, 1], [0, 1, 0]],      # T
    [[1, 1, 1], [1, 0, 0]],      # L
    [[1, 1, 1], [0, 0, 1]],      # J
    [[1, 1], [1, 1]],            # O
    [[0, 1, 1], [1, 1, 0]],      # S
    [[1, 1, 0], [0, 1, 1]]       # Z
]

# Define colors for each shape
shape_colors = [
    (0, 255, 255),    # Cyan (I)
    (128, 0, 128),    # Purple (T)
    (255, 165, 0),    # Orange (L)
    (0, 0, 255),      # Blue (J)
    (255, 255, 0),    # Yellow (O)
    (0, 255, 0),      # Green (S)
    (255, 0, 0)       # Red (Z)
]

# Initialize variables
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
score = 0

def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
            if grid[y][x] != 0:
                pygame.draw.rect(screen, shape_colors[grid[y][x] - 1], (x * GRID_SIZE + 1, y * GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2))

def draw_score():
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (20, 20))

def new_piece():
    shape_index = random.randint(0, len(shapes) - 1)
    shape = shapes[shape_index]
    color = shape_colors[shape_index + 1]
    piece = {"shape": shape, "color": color, "x": GRID_WIDTH // 2 - len(shape[0]) // 2, "y": 0}
    return piece

def draw_piece(piece):
    shape = piece["shape"]
    color = piece["color"]
    x = piece["x"]
    y = piece["y"]
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == 1:
                pygame.draw.rect(screen, color, ((x + j) * GRID_SIZE + 1, (y + i) * GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2))

def can_move(piece, dx, dy):
    shape = piece["shape"]
    x = piece["x"]
    y = piece["y"]
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == 1:
                new_x = x + j + dx
                new_y = y + i + dy
                if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or (new_y >= 0 and grid[new_y][new_x] != 0):
                    return False
    return True

def place_piece(piece):
    shape = piece["shape"]
    color = piece["color"]
    x = piece["x"]
    y = piece["y"]
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == 1:
                grid[y + i][x + j] = shape_colors.index(color) + 1

def remove_filled_rows():
    global score




import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Click the Ball Game")
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load('C:/Users/romfu/Desktop/csc_142/SOLO CODES/ball.png')


# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
MAX_SCORE = 5

score = 0
game_over = False
start_time = pygame.time.get_ticks()

def draw_text(surface, text, x, y, color, font_size=24):
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))
 
# 6 - Loop forever
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # Check if player clicked the ball
            if ballRect.collidepoint(event.pos):
                score += 1

                # Move ball to a new random location
                ballRect.left = random.randrange(MAX_WIDTH)
                ballRect.top = random.randrange(MAX_HEIGHT)

                # Randomly increase speed between 1 and 5
                xSpeed = abs(xSpeed) + random.randint(1, 5)
                ySpeed = abs(ySpeed) + random.randint(1, 5)
                # Randomize direction
                xSpeed *= random.choice([-1, 1])
                ySpeed *= random.choice([-1, 1])

                # Check for game over
                if score >= MAX_SCORE:
                    game_over = True
                    end_time = pygame.time.get_ticks()
                    elapsed_seconds = (end_time - start_time) / 1000
        if not game_over:
            if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
                xSpeed = -xSpeed
            if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
                ySpeed = -ySpeed
            ballRect.left += xSpeed
            ballRect.top += ySpeed

    # 7 - Draw everything
    window.fill(BLACK)
    if not game_over:
        window.blit(ballImage, ballRect)
    draw_text(window, f"Score: {score}", 10, 10, WHITE, 28)

    # 8 - Show game over message
    if game_over:
        draw_text(window, f"You clicked 5 times in {elapsed_seconds:.2f} seconds!", WINDOW_WIDTH//2 - 250, WINDOW_HEIGHT//2, WHITE,32)

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

# The png wasn't being foiund so I had to use a direct path to the image. You will need to change that path.



import pygame
import sys
import random
from math import sin

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3
GAME_LENGTH = 15

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  


def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Ball class
class Ball():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load('SOLO CODES/ball.png')
# A rect is made up of [x, y, width, height]
        self.ballRect = self.image.get_rect()
        self.width = self.ballRect.width
        self.height = self.ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
# Pick a random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = self.height
# Choose a random speed between -4 and 4, but not zero
# in both the x and y directions
        speedsList = [-7, -6, -5, -4, -3, 3, 4, 5, 6, 7]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.randrange(self.maxHeight, self.windowHeight * 2)
   
    def update(self):
# Check for hitting a wall. If so, change that direction.
        if (self.x < -self.width) or (self.x >= self.windowWidth):
            self.xSpeed = -self.xSpeed
# Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.windowHeight - self.ySpeed * sin(3.14 * self.x /
self.maxWidth)
        self.ballRect.x = self.x
        self.ballRect.y = self.y
    
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    # Each time through the loop, create a Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)  # append the new Ball to the list of Balls   

score = 0
startTicks = pygame.time.get_ticks()
lastSeconds = 0
gameOver = False

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            mousePos = event.pos

            for oBall in ballList[:]:
                if oBall.ballRect.collidepoint(mousePos):
                    ballList.remove(oBall)
                    score += 1
        if not gameOver:
                currentTicks = pygame.time.get_ticks()
                elapsedSeconds = (currentTicks - startTicks) // 1000
        
                # Add new ball every second
                if elapsedSeconds > lastSeconds:
                    lastSeconds = elapsedSeconds
                    newBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
                    ballList.append(newBall)
        
                # End game at 15 seconds
                if elapsedSeconds >= GAME_LENGTH:
                    gameOver = True
                    ballList.clear()

    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update()  # tell each Ball to update itself

   # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    for oBall in ballList:
        oBall.draw()   # tell each Ball to draw itself

    # 11 - Update the window
    pygame.display.update()
    draw_text(window, f"Score: {score}", 10, 10, WHITE, 28)
    draw_text(window, f"Time: {lastSeconds}", 10, 40, WHITE, 28)
    if gameOver:
        draw_text(
            window,
            f"Final Score: {score}",
            WINDOW_WIDTH // 2 - 100,
            WINDOW_HEIGHT // 2,
            YELLOW,
            40
        )

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
    

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

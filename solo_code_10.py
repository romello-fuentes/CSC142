import pygame
import pygwidgets
import random

# Initialize pygame
pygame.init()

# Window setup
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Reaction Time Game')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Clock
clock = pygame.time.Clock()

# UI Elements
startButton = pygwidgets.TextButton(window, (220, 300), 'Start Game')
messageDisplay = pygwidgets.DisplayText(window, (150, 50), '', fontSize=36)
reactionDisplay = pygwidgets.DisplayText(window, (150, 120), '', fontSize=32)

# Game States
WAITING_TO_START = 0
WAITING_RANDOM = 1
READY_TO_CLICK = 2
TOO_SOON = 3
SHOW_RESULT = 4

state = WAITING_TO_START

# Timer variables
startTime = 0
signalTime = 0
reactionTime = 0
randomDelay = 0

# Animation variables (circle pulse)
circleRadius = 20
growing = True

# Animated timer variables (NEW)
displayedTime = 0
countingUp = False
countStartTime = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start button
        if startButton.handleEvent(event):
            state = WAITING_RANDOM
            startTime = pygame.time.get_ticks()
            randomDelay = random.randint(2000, 5000)

            messageDisplay.setValue("Wait for green...")
            reactionDisplay.setValue("")

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            currentTime = pygame.time.get_ticks()

            if state == WAITING_RANDOM:
                state = TOO_SOON
                messageDisplay.setValue("Too soon! Click Start again.")

            elif state == READY_TO_CLICK:
                reactionTime = currentTime - signalTime
                state = SHOW_RESULT
                messageDisplay.setValue("Nice!")

                # Start animated count-up timer
                displayedTime = 0
                countStartTime = pygame.time.get_ticks()
                countingUp = True

    # State logic
    currentTime = pygame.time.get_ticks()

    if state == WAITING_RANDOM:
        if currentTime - startTime >= randomDelay:
            state = READY_TO_CLICK
            signalTime = pygame.time.get_ticks()

    # Animate result timer (NEW)
    if state == SHOW_RESULT and countingUp:
        elapsed = pygame.time.get_ticks() - countStartTime

        if elapsed < reactionTime:
            displayedTime = elapsed
        else:
            displayedTime = reactionTime
            countingUp = False

        reactionDisplay.setValue(f"{displayedTime / 1000:.3f} seconds")

    # Drawing
    window.fill(WHITE)

    # Pulsing circle animation
    if state in [WAITING_RANDOM, READY_TO_CLICK]:
        if growing:
            circleRadius += 1
            if circleRadius > 50:
                growing = False
        else:
            circleRadius -= 1
            if circleRadius < 20:
                growing = True

        if state == WAITING_RANDOM:
            pygame.draw.circle(window, RED, (300, 200), circleRadius)
        elif state == READY_TO_CLICK:
            pygame.draw.circle(window, GREEN, (300, 200), circleRadius)

    # Draw UI
    startButton.draw()
    messageDisplay.draw()
    reactionDisplay.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

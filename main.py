import pygame
import sys

# Constants
WIDTH = 800
HEIGHT = 600
TITLE = 'My Pygame Template'

FPS = 60 # FRAMES PER MINUTE

WHITE = (255, 255, 255) # RBG TRIPLET SAVED IN A TUPLE

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Clock Setup
clock = pygame.time.Clock() # Note the capital C in the word clock

# Game Loop
running = True
while running:
    # Listen for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Type the QUIT in UPPERCASE!
            running = False

# Game Logic
# (THIS is where you'll put your game's logic)
            
# Draw
    screen.fill(WHITE) #Fill screen background with white

# (This is where you'll draw your game objects)

    pygame.display.flip() # Update the display

# Limit frames per second (FPS)
clock.tick(FPS)

# Quit Pygame and exit system module 
pygame.quit()
sys.exit()
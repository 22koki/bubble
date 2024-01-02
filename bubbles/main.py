import pygame
from initialize import screen, pygame
from gameloop import game_loop

# Initialize pygame
pygame.init()

# Check the dimensions of the display surface
assert screen.get_width() > 0 and screen.get_height() > 0, "The display surface dimensions must be larger than 0x0"

# Main function
def main():
    # Start the game
    game_loop(screen)

if __name__ == "__main__":
    main()
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import config

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()

    # Open a new window
    size = (config.SCREEN_HEIGHT, config.SCREEN_WIDTH)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My First Game")

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carryOn = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carryOn = False  # Flag that we are done so we can exit the while loop

        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white.
        screen.fill(config.WHITE)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

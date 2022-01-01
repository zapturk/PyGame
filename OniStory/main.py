import pygame
import config
from game import Game
from game_state import GameState

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_HEIGHT, config.SCREEN_WIDTH))

pygame.display.set_caption("Oni Story")

# Clock to set the Frame Rate
clock = pygame.time.Clock()

game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
    # sets the Frame rate
    clock.tick(60)

    # Runs the update for the Game
    game.update()

    # Flips to the next frame
    pygame.display.flip()

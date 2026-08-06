"""
PythonQuest

Main entry point of the game.
Created by Anthony Allard.
"""

import pygame 
from states.menu import draw_menu

pygame.init()

WIDTH = 1920
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PythonQuest")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 

game_state = "MENU"

running = True

while running:
    if game_state == "MENU":
         draw_menu(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

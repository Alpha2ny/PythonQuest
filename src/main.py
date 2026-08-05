"""
PythonQuest

Main entry point of the game.
Created by Anthony Allard.
"""

import pygame

pygame.init()

WIDTH = 1920
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PythonQuest")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 64)
title = font.render("PythonQuest", True, WHITE)
title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2)) 

game_state = "MENU"

running = True

while running:
    if game_state == "MENU":
         screen.fill(BLACK)
         screen.blit(title, title_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

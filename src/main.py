"""
PythonQuest

Main entry point of the game.
Created by Anthony Allard.
"""

import pygame 
from states.menu import draw_menu
from states.chapter import draw_chapter_1
from states.story import draw_story_1
from systems.typewriter import Typewriter
from systems.dialogue import Dialogue 
from content.dialogue_data import DIALOGUES_STORY_1
from content.story_data import STORY_1_TEXT

pygame.init()

typewriter = Typewriter(character_display_time=50)
dialogues = Dialogue(DIALOGUES_STORY_1)

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
         draw_menu(screen, WIDTH, HEIGHT)

    elif game_state == "CHAPTER_1":
        draw_chapter_1(screen, WIDTH, HEIGHT)

    elif game_state == "STORY_1":
        draw_story_1(screen, WIDTH, HEIGHT, typewriter)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:

                if game_state == "MENU":
                    game_state = "CHAPTER_1"
                    
                elif game_state == "CHAPTER_1":
                    game_state = "STORY_1"
                    typewriter.reset_new_text(STORY_1_TEXT)
                    print("Chapter 1: Entering the game...")

                    line = dialogues.get_next_line()
                    typewriter.reset_new_text(line)

    pygame.display.flip()

pygame.quit()

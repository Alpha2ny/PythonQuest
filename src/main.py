"""
PythonQuest

Main entry point of the game.
Created by Anthony Allard.
"""

import pygame 

from states.menu import draw_menu
from states.chapter import draw_chapter
from states.story import draw_story
from content.story_data import STORY_1_TITLE
from systems.typewriter import Typewriter
from systems.dialogue import Dialogue 
from content.dialogue_data import DIALOGUES_STORY_1
from content.chapter_data import CHAPTER_1_TITLE, CHAPTER_1_INTRO

pygame.init()

typewriter = Typewriter(character_display_time=50)
dialogues = Dialogue(DIALOGUES_STORY_1)

story_data = {
    "title": STORY_1_TITLE
}

chapter_data = {
    "title": CHAPTER_1_TITLE,
    "intro": CHAPTER_1_INTRO
}

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
        draw_chapter(screen, WIDTH, HEIGHT, chapter_data)

    elif game_state == "STORY_1":
        draw_story(screen, WIDTH, HEIGHT, typewriter, story_data)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:

                if game_state == "MENU":
                    game_state = "CHAPTER_1"
                    
                elif game_state == "CHAPTER_1":
                    game_state = "STORY_1"

                    print("Chapter 1: Entering the game...")

                elif game_state == "STORY_1":
                    if not typewriter.is_finished():
                     typewriter.complete_text()
                    else:
                        next_line = dialogues.get_next_line()
                        if next_line is not None:
                            typewriter.reset_new_text(next_line)
                        else:
                            print("End of story reached.")
                            game_state = "MENU"
                   

    pygame.display.flip()

pygame.quit()

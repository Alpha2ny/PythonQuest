import pygame

def draw_chapter_1(screen, width, height):

    WHITE = (255, 255, 255)
    chapter_1_font = pygame.font.SysFont(None, 72)
    chapter_1_text = chapter_1_font.render("Chapter 1: The Beginning", True, WHITE)
    intro_font = pygame.font.SysFont(None, 48)
    chapter_1_intro = intro_font.render("Welcome, Future Python Hero!", True, WHITE)
    continue_font = pygame.font.SysFont(None, 36)
    continue_text = continue_font.render("Press ENTER to continue...", True, WHITE)
   
    chapter_1_rect = chapter_1_text.get_rect(center=(width // 2, height // 2))
    intro_rect = chapter_1_intro.get_rect(center=(width // 2, height // 2 + 100))
    continue_rect = continue_text.get_rect(center=(width // 2, height // 2 + 200))

    screen.fill((0, 0, 0))
    screen.blit(chapter_1_text, chapter_1_rect)
    screen.blit(chapter_1_intro, intro_rect)
    screen.blit(continue_text, continue_rect)


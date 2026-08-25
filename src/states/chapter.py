import pygame

def draw_chapter(screen, width, height, chapter_data):

    WHITE = (255, 255, 255)

    chapter_font = pygame.font.SysFont(None, 72)
    chapter_text = chapter_font.render(
    chapter_data["title"], 
    True, 
    WHITE
    )

    intro_font = pygame.font.SysFont(None, 48)
    chapter_intro = intro_font.render(
    chapter_data["intro"], 
     True, 
     WHITE
     )
    
    continue_font = pygame.font.SysFont(None, 36)
    continue_text = continue_font.render(
    "Press ENTER to continue...", 
    True, 
    WHITE
    )
   
    chapter_rect = chapter_text.get_rect(center=(width // 2, height // 2))
    intro_rect = chapter_intro.get_rect(center=(width // 2, height // 2 + 100))
    continue_rect = continue_text.get_rect(center=(width // 2, height // 2 + 200))

    screen.fill((0, 0, 0))
    screen.blit(chapter_text, chapter_rect)
    screen.blit(chapter_intro, intro_rect)
    screen.blit(continue_text, continue_rect)


import pygame

def draw_menu(screen, width, height):
    
    WHITE = (255, 255, 255)
    title_font = pygame.font.SysFont(None, 72)
    menu_font = pygame.font.SysFont(None, 48)
    subtitle_font = pygame.font.SysFont(None, 36)
    subtitle_font.set_italic(True) 

    title = title_font.render("PythonQuest", True, WHITE)
    start_game = menu_font.render("Press Enter to Start", True, WHITE)
    subtitle = subtitle_font.render("Learn Python.", True, WHITE)
    subtitle2 = subtitle_font.render("Become a Hero.", True, WHITE)

    title_rect = title.get_rect(center=(width // 2, height // 4))
    subtitle_rect = subtitle.get_rect(center=(width // 2, height // 3 + 70))
    subtitle2_rect = subtitle2.get_rect(center=(width // 2, height // 3 + 110))
    start_game_rect = start_game.get_rect(center=(width // 2, height // 2 + 100))
  

    screen.fill((0, 0, 0))
    screen.blit(title, title_rect)
    screen.blit(subtitle, subtitle_rect)
    screen.blit(subtitle2, subtitle2_rect)
    screen.blit(start_game, start_game_rect)


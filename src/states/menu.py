import pygame

def draw_menu(screen):

    print("Menu")
    
    WHITE = (255, 255, 255)
    font = pygame.font.SysFont(None, 64)
    title = font.render("PythonQuest", True, WHITE)
    title_rect = title.get_rect(center=(640, 360))

    screen.fill((0, 0, 0))
    screen.blit(title, title_rect)
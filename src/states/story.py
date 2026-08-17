import pygame

def draw_story_1(screen, width, height, typewriter):

    current_time = pygame.time.get_ticks()

    typewriter.update(current_time)

    visible_text = typewriter.get_visible_text()

    WHITE = (255, 255, 255)

    story_1_font = pygame.font.SysFont(None, 72)
    story_1_text = story_1_font.render(
        "Story 1: The Adventure Begins",
        True,
        WHITE
    )

    story_font = pygame.font.SysFont(None, 48)
    story_1_intro = story_font.render(
        visible_text,
        True,
        WHITE
    )

    continue_font = pygame.font.SysFont(None, 36)
    continue_text = continue_font.render(
        "Press ENTER to continue...",
        True,
        WHITE
    )

    story_1_rect = story_1_text.get_rect(
        center=(width // 2, height // 2)
    )

    intro_rect = story_1_intro.get_rect(
        center=(width // 2, height // 2 + 100)
    )

    continue_rect = continue_text.get_rect(
        center=(width // 2, height // 2 + 200)
    )

    screen.fill((0, 0, 0))

    screen.blit(story_1_text, story_1_rect)
    screen.blit(story_1_intro, intro_rect)
    screen.blit(continue_text, continue_rect)
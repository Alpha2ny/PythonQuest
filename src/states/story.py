import pygame

def draw_story(screen, width, height, typewriter, story_data):

    current_time = pygame.time.get_ticks()

    typewriter.update(current_time)

    visible_text = typewriter.get_visible_text()

    WHITE = (255, 255, 255)

    story_font = pygame.font.SysFont(None, 72)
    story_text = story_font.render(
        story_data["title"],
        True,
        WHITE
    )

    story_font = pygame.font.SysFont(None, 48)
    story_dialogue = story_font.render(
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

    dialogue_rect = story_text.get_rect(
        center=(width // 2, height // 2)
    )

    intro_rect = story_dialogue.get_rect(
        center=(width // 2, height // 2 + 100)
    )

    continue_rect = continue_text.get_rect(
        center=(width // 2, height // 2 + 200)
    )

    screen.fill((0, 0, 0))

    screen.blit(story_text, dialogue_rect)
    screen.blit(story_dialogue, intro_rect)
    screen.blit(continue_text, continue_rect)
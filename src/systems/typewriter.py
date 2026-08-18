class Typewriter:
    def __init__(self, character_display_time=50):
        self.text = ""
        self.characters_displayed = 0
        self.character_display_time = character_display_time
        self.last_character_time = 0

    def reset_new_text(self, new_text):
        self.text = new_text
        self.characters_displayed = 0
        self.last_character_time = 0

    def update(self, current_time):
        if current_time - self.last_character_time >= self.character_display_time:
            if self.characters_displayed < len(self.text):
                self.characters_displayed += 1
                self.last_character_time = current_time

    def get_visible_text(self):
        return self.text[:self.characters_displayed]

    def is_finished(self):
        return self.characters_displayed >= len(self.text)

    def complete_text(self):
        self.characters_displayed = len(self.text)
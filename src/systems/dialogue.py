class dialogue:
    def __init__(self, dialogue_data):
        self.dialogue_data = dialogue_data
        self.current_index = 0

    def get_next_line(self):
        if self.current_index < len(self.dialogue_data):
            line = self.dialogue_data[self.current_index]
            self.current_index += 1
            return line
        else:
            return None
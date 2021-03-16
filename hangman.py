class HangManGame:
    def __init__(self, word):
        self.word = word.strip()
        self.wrong_choices_left = 3
        self.guesses = set()

    def is_valid_guess(self, letter):
        return len(letter) == 1

    def guess(self, letter):
        self.guesses.add(letter)
        if self.word.find(letter) < 0:
            self.wrong_choices_left -= 1

    def show_found(self):
        """Format word by replacing letters not found with _"""
        filtered = ''
        for index in range(0, len(self.word)):
            if self.word[index] in self.guesses:
                filtered += self.word[index]
            else:
                filtered += '_'

        return filtered

    def has_found_all_letters(self):
        """Return whether a word has been guessed"""
        for index in range(0, len(self.word)):
            if self.word[index] not in self.guesses:
                return False
        return True

    def is_game_over(self):
        return self.has_found_all_letters() or self.wrong_choices_left < 0

    def prompt(self):
        line = f"{self.show_found()}\n"
        line += f"tried: {sorted(self.guesses)}\n"
        line += f"wrong choices left: {self.wrong_choices_left}\n"
        return line

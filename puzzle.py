import random

class Puzzle:
    
    def __init__(self):
        self._word_list = ['frog', 'apple', 'people']
        self._word_selected = ''

        self._word_guess = ['_ '] * len(self._word_selected)
    
    def _select_word(self):
        pass

    def draw_word_guess(self):
        pass

    def process_guess(self, guess_letter):
        pass

    def can_keep_guessing(self):
        pass
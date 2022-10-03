import random


class Puzzle:
    
    def __init__(self):
        self._word_list = ['frog', 'apple', 'people']
        self._word_selected = ''
        self._word_guess = '_ ' * len(self._word_selected)
        self._guesses = []
        self._fails = []
        self._letters = []
        self.failure = 0
    
    #def _select_word(self):
        #self._word_selected = random.choice(self._word_list)

    def draw_word_guess(self):
        self._word_selected = random.choice(self._word_list)
        space = len(self._word_selected)
        for i in range(space):
            print('_ ', end=" ")
        
        for letter in self._word_selected:
            self._letters.append(letter)
        


    def process_guess(self, guess_letter):
        self._guesses.append(guess_letter)

        for guess_letter in self._word_selected:
            if guess_letter in self._guesses:
                print(guess_letter, end=" ")
            else:
                print('_ ', end=" ")
        
    def return_fail(self, guess_letter):
        
        if guess_letter not in self._letters:
            self.failure += 1
            return self.failure
        elif guess_letter in self._letters:
            self.failure += 0
            return self.failure
            

    #def can_keep_guessing(self):
        #if self.tries != 0:
            #return True
        #else:
            #return False
        
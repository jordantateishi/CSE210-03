from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    """

    def __init__(self):

        self._is_playing = True
        self._puzzle = Puzzle()
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        #self.failures = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.failures = 0
        self._puzzle.draw_word_guess()
        self._jumper.drawing(self.failures)

        while self._is_playing:
            self._get_inputs()
            self._do_updates(self._get_inputs)
            self._do_outputs()
        print('\ngame over')

    def _get_inputs(self):
       
        guess_letter = self._terminal_service.read_text('\nGuess a letter [a-z]: ')
        self._puzzle.process_guess(guess_letter)
        return guess_letter
       
    def _do_updates(self, guess_letter):
        self.failures = self._puzzle.return_fail(guess_letter)
        self._jumper.drawing(self.failures) 
        
    def _do_outputs(self):
        
        if self.failures == 5:
            self._is_playing = False
            print('Game over')

        
       
from game.card import Card


class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

#Lewis ->
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.previous = 0
        self.current = Card()
        self.hi_lo = ""
        self.total_score = 300
        self.first_turn = True


#Don't Change ->
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


#Lewis ->
    def get_inputs(self):
        """Ask the user if they want to roll. Draw a card before the first turn.

        Args:
            self (Director): An instance of Director.
        """
        if self.first_turn:
            temp_card = Card()
            temp_card.pick()
            self.previous = temp_card.value
            print(f"Let's begin. Your starting score is {self.total_score}")
            print(f"Your first card is {self.previous}")
        
        self.hi_lo = input("Higher or lower? [h/l] ").lower()
        #self.is_playing = (self.hi_lo == "h")
        


#Christopher ->       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if self.first_turn:
            self.first_turn = False
        else:
            self.previous = self.current.value
        
        # Add to the total score (100, -75, 0)

        self.current.pick()
        
        if self.hi_lo == 'h' and self.current.value > self.previous:
            self.total_score += 100
        elif self.hi_lo == 'h' and self.current.value < self.previous:
            self.total_score += -75
        elif self.hi_lo == 'l' and self.current.value > self.previous:
            self.total_score += -75
        elif self.hi_lo == 'l' and self.current.value < self.previous:
            self.total_score += 100
        else:
            self.total_score += 0


#Christopher ->       
    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to draw again. 

        Args:
            self (Director): An instance of Director.
        """
        if self.total_score <= 0:
            self.is_playing = False
            print(f"You lose. Your score is {self.total_score}")
        
        print(f"You drew {self.current.value}")
        print(f"Your score is: {self.total_score}")
        keep_playing = input("Draw again? [y/n] ")
        self.is_playing = (keep_playing == "y")
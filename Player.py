import math
import random

#this is the base player class on top of which we 
#will build a randomcomputerplayer and a humanplayer using
#inheritance 

class Player:
    # letter is x or o
    def __init__(self, letter):
        self.letter = letter

    # we want all players to get their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return super().get_move(game)

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
        
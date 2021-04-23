# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:51:53 2021

@author: Andrej Cop Prek
"""

import random

class Rock_Paper_Scissors:
    """
    Class for Rock Paper Scissors game
    """
    
    def __init__(self, valid_input = [], Rock='Rock', Paper='Paper', Scissors='Scissors'):
        """

        :param valid_input:
        :param Rock:
        :param Paper:
        :param Scissors:
        """

        self.Rock = Rock
        self.Paper = Paper
        self.Scissors = Scissors
        
        self.valid_input = [self.Rock, self.Paper, self.Scissors]
        
        print('To pick a choice and battle, execute self.pick_one({your choice as str}) \n')
        print('Use self.valid_input to check what are the available values to use')
        
        
    def pick_one(self, players_choice):
        
        # input is a player's choice for Rock, Paper, Scissors game
        self.players_choice = players_choice
        
        # throw an error in case the input is none of these 3 values
        assert players_choice in self.valid_input #"You must select either Rock, Paper or Scissors"
        
        # computer picks a random choice from the list of valid inputs
        self.computers_choice = random.choice(self.valid_input)
        
        if self.players_choice == self.computers_choice:
            print('It is a tie! Computer also picked ' + self.computers_choice)
        # if you chose rock:
        elif self.players_choice == 'Rock' and self.computers_choice == 'Scissors':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Rock crushes Scissors')
        elif self.players_choice == 'Rock' and self.computers_choice == 'Paper':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Paper covers Rock')    
        # if you chose paper
        elif self.players_choice == 'Paper' and self.computers_choice == 'Rock':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Paper covers Rock')         
        elif self.players_choice == 'Paper' and self.computers_choice == 'Scissors':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Scissors cut Paper')        
        # if you chose scissors
        elif self.players_choice == 'Scissors' and self.computers_choice == 'Paper':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Scissors cut Paper')        
        elif self.players_choice == 'Scissors' and self.computers_choice == 'Rock':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Rock crushes Scissors')    
    
class Rock_Paper_Scissors_Lizard_Spock(Rock_Paper_Scissors):
      
    def __init__(self, valid_input = [], Rock='Rock', Paper='Paper', Scissors='Scissors', Lizard='Lizard', Spock='Spock'):
        super(Rock_Paper_Scissors_Lizard_Spock, self).__init__(self) #, valid_input, Rock, Paper, Scissors)
        self.Lizard = Lizard
        self.Spock = Spock
        
        self.valid_input.append(self.Lizard)
        self.valid_input.append(self.Spock)


    def pick_one(self, players_choice):

        assert players_choice in self.valid_input #"You must select either Rock, Paper or Scissors, Lizard or Spock"
        
        super(Rock_Paper_Scissors_Lizard_Spock, self).pick_one(players_choice)
    
        # extend the code for Lizard and Spock :)
    
        # if you chose rock
        if self.players_choice == 'Rock' and self.computers_choice == 'Lizard':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Rock crushes Lizard')
        elif self.players_choice == 'Rock' and self.computers_choice == 'Spock':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Spock vaporizes Rock')    
        # if you chose paper
        elif self.players_choice == 'Paper' and self.computers_choice == 'Lizard':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Lizard eats Paper')      
        elif self.players_choice == 'Paper' and self.computers_choice == 'Spock':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Paper covers Spock')           
        # if you chose scissors
        elif self.players_choice == 'Scissors' and self.computers_choice == 'Lizard':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Scissors decapitates Lizard')        
        elif self.players_choice == 'Scissors' and self.computers_choice == 'Spock':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Spock smashes Scissors')
        # if you chose Lizard
        elif self.players_choice == 'Lizard' and self.computers_choice == 'Rock':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Rock crushes Lizard')      
        elif self.players_choice == 'Lizard' and self.computers_choice == 'Paper':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Lizard eats Paper')
        elif self.players_choice == 'Lizard' and self.computers_choice == 'Scissors':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Scissors decapitates Lizard')   
        elif self.players_choice == 'Lizard' and self.computers_choice == 'Spock':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Lizard poisons Spock')
        # if you chose Spock
        elif self.players_choice == 'Spock' and self.computers_choice == 'Rock':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Spock vaporizes Rock')      
        elif self.players_choice == 'Spock' and self.computers_choice == 'Paper':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Paper covers Spock')
        elif self.players_choice == 'Spock' and self.computers_choice == 'Scissors':
            print ('You won! :) Computer chose ' + self.computers_choice + '. Spock smashes Scissors')   
        elif self.players_choice == 'Spock' and self.computers_choice == 'Lizard':
            print ('You lost :( Computer chose ' + self.computers_choice + '. Lizard poisons Spock')
         

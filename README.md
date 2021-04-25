# ARPSLS

# Overview
Files for PyPi Package to play rock, paper, scissors, lizard, spock game - this is just for fun.

# How to Run It
1) First you should downlaod the package by calling the following command in your console.
> pip install arpsls
2) Then import the package with *import arpsls*
3) You can play either normal rock-paper-scissors or extended rock-paper-scissors-lizard-spock game
	- For rock-paper-scissors run the following command in python console (you can replace "RPS" with a name of your choice):
		> from arpsls.RockPaperScissorsLizardSpock import Rock_Paper_Scissors as RPS
	- For rock-paper-scissors-lizard-sprock run the following command in python console (you can replace "RPSLS" a name of your choice):
		> from arpsls.RockPaperScissorsLizardSpock import Rock_Paper_Scissors_Lizard_Spock as RPSLS
4) To initiate an instance of selected class run:
> my_game = RPS()

for rock-paper-scissors game or
> my_game = RPSLS()

for rock-paper-scissors-lizard_spock game.

5) To get the list of valid inputs run the following command in python console:
> my_game.valid_input
6) To play the game run the following command in python console:
> my_game.pick_one('abc')

where 'abc' should be replaced with one of the valid inputs

7) Enjoy this amazing game :)
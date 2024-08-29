#Rock Paper Scissors Game
from random import randint
#Moves for the player
moves = ["rock", "paper", "scissors"] # List all possible moves in a List
while True: # True must have capital T
    computer = moves[randint(0,2)]
    player = str(input("Rock, Paper, or Scissors...or end game? ").lower()) #nice feature that means any input, with upper case or lower case initial, is accepted. Note the additional space after the question too - makes the code look a bit nicer
    if player == "end the game":
        print("The game has ended")
        break # breaks the while true loop, stopping it completely.
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You Lose!", computer, "beats", player)
        else:
            print("You Win!", player, "beats", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You Lose!", computer, "beats", player)
        else:
            print("You Win!", player, "beats", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You Lose!", computer, "beats", player)
        else:
            print("You Win!", player, "beats", computer)  #Have designed this code in a way that makes it easy to copy and paste certain parts
    else:
        print("Check your spelling")
        
#how to take game to next level: points scoring system

    
    


from random import randint

choices = ["Rock","Paper","Scissors"]

computer = choices[randint(0, 2)]

playerPoints = 0
computerPoints = 0

goOn = True

while(goOn):

    player = input("Rock, Paper or Scissors? or enter Finish to end!\n")
    
    if (player == "Finish"):
        goOn = False
    
    elif (player == computer):
        print("Tie!")
    
    elif (player == "Rock"):
        if (computer == "Paper"):
            # computer rolls paper and wins the game
            print("You lose!", computer, "covers", player)
            computerPoints += 1
        else:
            
            print("You win!", player, "smashes", computer)
            playerPoints += 1
   
    elif (player == "Scissor"):
        if (computer == "Rock"):
           
            print("You lose!", computer, "smashes", player)
            computerPoints += 1
        else:
            
            print("You win!", player, "cuts", computer)
            playerPoints += 1
    
    elif (player == "Paper"):
        if (computer == "Scissors"):
            
            print("You lose!", computer, "cuts", player)
            computerPoints += 1
        else:

            print("You win!", player, "covers", computer)
            playerPoints += 1
    else:
        print("That is not a valid play. Check your spelling!")

    
    computer = choices[randint(0, 2)]
    print("********Next Turn*********")


print("*******Final Points********")
print("Player Points: ", playerPoints)
print("Computer Points: ", computerPoints)

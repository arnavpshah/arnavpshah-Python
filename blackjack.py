import time
import random

input("Welcome to my Casino. Click any key to play Blackjack: ")

while True:
  phand = []
  for i in range(2):
    phand.append(random.randint(2,11))
  print("Here is your hand:  ")
  print(phand)
  game = True
  if sum(phand) == 21:
    print("You won")
    game = False
  while True:
    play = input("Type h to hit or s to stay: ")
    if play == "h":
      phand.append(random.randint(2,11))
      print("Here is your hand: ")
      print(phand)
      if sum(phand) > 21:
        print("You busted")
        game = False
        break
      elif sum(phand) == 21:
        print("You won")
        game = False
        break
    else:
      break


  if game == True:
    print("Dealers Turn")
    chand = []
    for i in range(2):
      chand.append(random.randint(2,11))
    print("Here is the Dealers hand: ")
    print(chand)
    while True:
      if sum(chand) < 16:
        chand.append(random.randint(2,11))
        print("The dealer hit")
        print(chand)
      elif sum(chand) == 21:
        print("The dealer go Blackjack, You lose")
        break
      elif sum(chand) > 21:
        print("The dealer Busted, You win")
        break
      else:
        print("The dealer has finallized his hand")
        if sum(phand) > sum(chand):
          print("You win")
          break
        elif sum(phand) < sum(chand):
          print("The dealer wins")
          break
        else:
          break
  input("Press any key to play again: ")

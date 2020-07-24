# Play an immediate win
# Block an opponent's immediate win
# Play a fork
# Block an opponent’s fork
# Play center
# Play corners
# Play sides


import random
board = [[" "," "," "],[" "," ", " "],[" "," "," "]]
def printBoard(board):
  for row in range(3):
    for col in range(3):
      if col == 2:
        print(" "+board[row][col])
      else:
        print(" "+board[row][col] + " |",end="")
    if row != 2:
      print("---+---+---")
  print("")

def win(board, p):
  # horizontal wins
  for row in range(3):
    count = 0 
    for col in range(3):
      if board[row][col] == p:
        count += 1
    if count == 3:
      return True
  # verticals
  for col in range(3):
    count = 0 
    for row in range(3):
      if board[row][col] == p:
        count += 1
    if count == 3:
      return True
  # diagonals
  if board[0][0] == p and board[1][1] == p and board[2][2] == p:
    return True
  if board[0][2] == p and board[1][1] == p and board[2][0] == p:
    return True
  

def full(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == " ":
        return False
  return True

def randomCompmove(board):
  while True:
    row = random.randint(0,2)
    col = random.randint(0,2)
    if board[row][col] == " ":
      return [row, col]

flip=random.randint(0,1)
if flip==1:
  print("The computer is X and will play first")
  player='O'
  comp = 'X'
else:
  print("You are X and will play first")
  player='X'
  comp= 'O'

while True:
  if flip == 0:
    printBoard(board)
    while True:
      row = int(input("What row do you want to put your X/O on: "))-1
      col = int(input("What column do you want to put your X/O on: "))-1
      if row >= 0 and row <= 2 and col >= 0 and col <= 2 and board[row][col] == " ":
        board[row][col] = player
        break
      else:
        print("INVALID OPTION")
    if win(board,player):
      print("You win!")
      break
  else:
    play = randomCompmove(board)
    board[play[0]][play[1]] = comp
    if win(board, comp):
      print("You lose")
      break
  if full(board):
    print("Tie")
    break
  # change turns
  if flip == 0:
    flip = 1
  else:
    flip = 0
printBoard(board)

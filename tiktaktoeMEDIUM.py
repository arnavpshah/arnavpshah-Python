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
  # making the board
  for row in range(3):
    for col in range(3):
      if col == 2:
        # making rows
        print(" "+board[row][col])
      else:
        # making columns
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
  
def check(board, row, col, p):
  if board[row][col] != " ":
    return False
  # making a duplicate of board
  duplicate = []
  for i in range(3):
    new = []
    for j in range(3):
      new.append(board[i][j])
    duplicate.append(new)
  duplicate[row][col]=p
  return(win(duplicate, p))

def AIMove(board, c, p):
  # computer goes for win
  for row in range(3):
    for col in range(3):
      if check(board, row, col, c):
        return[row, col]
  # computer goes for block
  for row in range(3):
    for col in range(3):
      if check(board, row, col, p):
        return[row, col]
  # computer goes for center
  if board[1][1] == " ":
    return [1,1]
  # computer goes for corner
  if board[0][0] == " ":
    return [0,0]
  elif board[0][2] == " ":
    return [0,2]
  elif board[2][0] == " ":
    return [2,0] 
  elif board[2][2] == " ":
    return [2,2]
  # computer makes random move
  while True:
    row = random.randint(0,2)
    col = random.randint(0,2)
    if board[row][col] == " ":
      return [row, col]

def full(board):
  # the game board is full and the game is a tie
  for row in range(3):
    for col in range(3):
      if board[row][col] == " ":
        return False
  return True

flip=random.randint(0,1)
# X plays first and it randomizes who goes first
if flip==1:
  print("The computer is X and will play first")
  player='O'
  comp = 'X'
else:
  print("You are X and will play first")
  player='X'
  comp= 'O'

while True:
  # the computer's moves
  if flip == 0:
    printBoard(board)
    while True:
      # where the computer is going to put his move
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
    play = AIMove(board, comp, player)
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

from random import randint
import os

print("Welcome to the Tic Tac Toe Game !!\nYou will be playing against computer !!!\n")

my_player = int(input("Type 1 if you want to play first or press 2 if you want to play second: "))
computer_player = None  

mat = [["-","-","-"],["-","-","-"],["-","-","-"]]
  
if my_player == 1:
    x_player = my_player
    o_player = computer_player
else:
    o_player = my_player
    x_player = computer_player
  
os.system("clear")
  
def table(mat):
  print("\n    ")
  for i in range(0,3):
    for j in range(0,3):
      if j < 2:
        print(f"  {mat[i][j]}  |", end=" ")
      else:
        print(f"  {mat[i][j]}")
    if i == 0 or i == 1:
      print("-------------------")
  print("\n")

def x_player_move(mat):
  if x_player == my_player:
    table(mat)
    row = int(input("Enter row (1, 2 or 3): "))
    column = int(input("Enter column (1, 2 or 3): "))
    while mat[row-1][column-1] != "-":
      os.system("clear")
      print("Try another position !!")
      table(mat)
      row = int(input("Enter row (1, 2 or 3): "))
      column = int(input("Enter column (1, 2 or 3): "))
    return [row,column]
  else:
    row = randint(0,3)
    column = randint(0,3)
    while mat[row-1][column-1] != "-":
      row = randint(0,3)
      column = randint(0,3)
    return [row,column]
    
def o_player_move(mat):
  table(mat)
  if o_player != my_player:
    row = randint(0,3)
    column = randint(0,3)
    while mat[row-1][column-1] != "-":
      row = randint(0,3)
      column = randint(0,3)
    return [row,column]
  else:
    row = int(input("Enter row (1, 2 or 3): "))
    column = int(input("Enter column (1, 2 or 3): "))
    while mat[row-1][column-1] != "-":
      os.system("clear")
      print("Try another position !!")
      table(mat)
      row = int(input("Enter row (1, 2 or 3): "))
      column = int(input("Enter column (1, 2 or 3): "))
    return [row,column]

def x_win(mat):
  if mat[0][0]=="X" and mat[1][1]=="X" and mat[2][2]=="X" or mat[0][0]=="X" and mat[1][0]=="X" and mat[2][0]=="X" or mat[0][0]=="X" and mat[0][1]=="X" and mat[0][2]=="X" or mat[0][2]=="X" and mat[1][2]=="X" and mat[2][2]=="X" or mat[2][0]=="X" and mat[2][1]=="X" and mat[2][2]=="X" or mat[1][0]=="X" and mat[1][1]=="X" and mat[1][2]=="X" or mat[0][1]=="X" and mat[1][1]=="X" and mat[2][1]=="X" or mat[0][2]=="X" and mat[1][1]=="X" and mat[2][0]=="X":
    return True
  else:
    return False

def o_win(mat):
  if mat[0][0]=="O" and mat[1][1]=="O" and mat[2][2]=="O" or mat[0][0]=="O" and mat[1][0]=="O" and mat[2][0]=="O" or mat[0][0]=="O" and mat[0][1]=="O" and mat[0][2]=="O" or mat[0][2]=="O" and mat[1][2]=="O" and mat[2][2]=="O" or mat[2][0]=="O" and mat[2][1]=="O" and mat[2][2]=="O" or mat[1][0]=="O" and mat[1][1]=="O" and mat[1][2]=="O" or mat[0][1]=="O" and mat[1][1]=="O" and mat[2][1]=="O" or mat[0][2]=="O" and mat[1][1]=="O" and mat[2][0]=="O":
    return True
  else:
    return False


def game():

  moves = 0
  while True:

      moves += 1
      position_x = x_player_move(mat)
      mat[position_x[0]-1][position_x[1]-1] = "X"
    
      if x_win(mat):
        os.system("clear")
        table(mat)
        if my_player == x_player:
          print("You've won !!")
        else:
          print("You've lost")
        break

      if moves == 9:
        os.system("clear")
        table(mat)
        print("Tied Round")
        break
    
      moves += 1
      position_o = o_player_move(mat)
      mat[position_o[0]-1][position_o[1]-1] = "O"
    
      if o_win(mat):
        os.system("clear")
        table(mat)
        if my_player == o_player:
          print("You've won !!")
        else:
          print("You've lost")
        break

      os.system("clear")


game()

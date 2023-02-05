from random import randint


mat = [["-","-","-","-","-","-"],["-","-","-"," - ","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"]]


def write(mat): # printing tic-tac-toe table
    print("     -------------------------")
    for i in range(0,3):
        for j in range(0,3):
            if j != 2:
                print(f"    |   {mat[i][j]}",end="")
            else:
                print(f"    |   {mat[i][j]}   |")
        print("     -------------------------")


def check(mat,my_player): # checking if one of the players has won
    for i in range(0,3):
        for j in range(0,3):
            if mat[i][j] == "X" and mat[i][j + 1] == "X" and mat[i][j + 2] == "X" or mat[i][j] == "X" and mat[i + 1][j] == "X" and mat[i + 2][j] == "X" or mat[i][j] == "X" and mat[i + 1][j + 1] == "X" and mat[i + 2][j + 2] == "X":
                write(mat)
                if my_player == 1:
                    print("You won !!")
                else:
                    print("You lost !!")
                return 1
            elif mat[i][j] == "O" and mat[i][j + 1] == "O" and mat[i][j + 2] == "O" or mat[i][j] == "O" and mat[i + 1][j] == "O" and mat[i + 2][j] == "O" or mat[i][j] == "O" and mat[i + 1][j + 1] == "O" and mat[i + 2][j + 2] == "O":
                write(mat)
                if my_player == 2:
                    print("You won !!")
                else:
                    print("You lost !!")
                return 2
    number_of_moves = 0
    for i in range(0,3):
        for j in range(0,3):
            if mat[i][j] != "-":
                number_of_moves += 1
    if number_of_moves == 9:
        write(mat)
        print("Tied !!")
        return 0
    return -1


print("Welcome to the Tic Tac Toe Game !!\nYou will be playing against computer !!!\n")
my_player = int(input("Do you want to be X-player or O-player (type 1 for X, type 2 for Y): "))

while True:

    if my_player == 1: # if my player is X
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        while mat[row][column] != "-":
            print("That field is filled !!")
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))
        mat[row][column] = "X"
        if check(mat,my_player) == 1 or check(mat,my_player) == 2 or check(mat,my_player) == 0:
            break
        comp_row = randint(0,2)
        comp_column = randint(0,2)
        while mat[comp_row][comp_column] != "-":
            comp_row = randint(0, 2)
            comp_column = randint(0, 2)
        mat[comp_row][comp_column] = "O"
        if check(mat,my_player) == 1 or check(mat,my_player) == 2 or check(mat,my_player) == 0:
            break
        write(mat)

    else: #if my player is O
        comp_row = randint(0, 2)
        comp_column = randint(0, 2)
        while mat[comp_row][comp_column] != "-":
            comp_row = randint(0, 2)
            comp_column = randint(0, 2)
        mat[comp_row][comp_column] = "X"
        if check(mat, my_player) == 1 or check(mat, my_player) == 2 or check(mat, my_player) == 0:
            break
        write(mat)
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        while mat[row][column] != "-":
            print("That field is filled !!")
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))
        mat[row][column] = "O"
        if check(mat, my_player) == 1 or check(mat, my_player) == 2 or check(mat, my_player) == 0:
            break

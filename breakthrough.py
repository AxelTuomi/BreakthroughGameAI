#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

def game(cordinates_0, cordinates_X, victoryCordinates_0, victoryCordinates_X, possibleCordinates):
    board(cordinates_0, cordinates_X)
    while True:
        movechoices = []
        step = []
        
        for i in range(0, len(cordinates_0)):
            if cordinates_0[i] - 9 in cordinates_X:
                movechoices = movechoices + [eliminatingLeft_0]
                step = step + [i]
                #Victory checker
                #If 0 wins by eliminating X on it's left, execute it
                if cordinates_0[i] - 9 in victoryCordinates_0:
                    eliminatingLeft_0(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("0 won!")
                    return
                
            if cordinates_0[i] + 11 in cordinates_X:
                movechoices = movechoices + [eliminatingRight_0]
                step = step + [i]
                #Victory checker
                #If 0 wins by eliminating X on it's right, execute it
                if cordinates_0[i] + 11 in victoryCordinates_0:
                    eliminatingRight_0(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("0 won!")
                    return
                
            if cordinates_0[i] + 1 not in cordinates_X and cordinates_0[i] + 1 not in cordinates_0:
                movechoices = movechoices + [forward_0]
                step = step +[i]
                #Victory checker
                #If 0 wins by moving forward, execute it
                if cordinates_0[i] + 1 in victoryCordinates_0:
                    forward_0(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("0 won!")
                    return

            if cordinates_0[i] + 11 not in cordinates_0 and cordinates_0[i] + 11 not in cordinates_X and cordinates_0[i] + 11 in possibleCordinates:
                movechoices = movechoices + [diagonalRight_0]
                step = step + [i]
                #Victory checker 
                #If 0 wins by moving diagonally right, execute it
                if cordinates_0[i] + 11 in victoryCordinates_0:
                    diagonalRight_0(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("0 won!")
                    return

            if cordinates_0[i] - 9 not in cordinates_0 and cordinates_0[i] - 9 not in cordinates_X and cordinates_0[i] - 9 in possibleCordinates:
                movechoices = movechoices + [diagonalLeft_0]
                step = step + [i]
                #Victory checker
                #If 0 wins by moving diagonally left, execute it
                if cordinates_0[i] - 9 in victoryCordinates_0:
                    diagonalLeft_0(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("0 won!")
                    return
                
        if len(movechoices) == 0:
            Stalemate(cordinates_0, cordinates_X)

        random_val(cordinates_0, cordinates_X, i, movechoices, step, human)    
        
        #Resets the lists
        movechoices = []
        step = []
        
        for i in range(0, len(cordinates_X)):
            if cordinates_X[i] + 9 in cordinates_0:
                movechoices = movechoices + [eliminatingLeft_X]
                step = step + [i]
                #Victory checker
                #If X wins by eliminating 0 on it's left, execute it
                if cordinates_X[i] + 9 in victoryCordinates_X:
                    eliminatingLeft_X(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("X won!")
                    return
                
            if cordinates_X[i] - 11 in cordinates_0:
                movechoices = movechoices + [eliminatingRight_X]
                step = step + [i]
                #Victory checker
                #If X wins by eliminating 0 on it's right, execute it
                if cordinates_X[i] - 11 in victoryCordinates_X:
                    eliminatingRight_X(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("X won!")
                    return
                
            if cordinates_X[i] - 1 not in cordinates_0 and cordinates_X[i] - 1 not in cordinates_X:
                movechoices = movechoices + [forward_X]
                step = step +[i]
                #Victory checker
                #If X wins by moving forward, execute it
                if cordinates_X[i] - 1 in victoryCordinates_X:
                    forward_X(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("X won!")
                    return

            if cordinates_X[i] - 11 not in cordinates_0 and cordinates_X[i] - 11 not in cordinates_X and cordinates_X[i] - 11 in possibleCordinates:
                movechoices = movechoices + [diagonalRight_X]
                step = step + [i]
                #Victory checker
                #If X wins by moving diagonally right, execute it
                if cordinates_X[i] - 11 in victoryCordinates_X:
                    diagonalRight_X(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("X won!")
                    return

            if cordinates_X[i] + 9 not in cordinates_0 and cordinates_X[i] + 9 not in cordinates_X and cordinates_X[i] + 9 in possibleCordinates:
                movechoices = movechoices + [diagonalLeft_X]
                step = step + [i]
                #Victory checker
                #If X wins by moving diagonally left, execute it
                if cordinates_X[i] + 9 in victoryCordinates_X:
                    diagonalLeft_X(cordinates_0, cordinates_X, i)
                    board(cordinates_0, cordinates_X)
                    print("X won!")
                    return
            
        if len(movechoices) == 0:
            Stalemate(cordinates_0, cordinates_X)
            
        random_val(cordinates_0, cordinates_X, i, movechoices, step, False)

#Methods of all moves
def forward_0(cordinates_0, cordinates_X, i):
    cordinates_0[i] = cordinates_0[i] + 1

def diagonalRight_0(cordinates_0, cordinates_X, i):
    cordinates_0[i] = cordinates_0[i] + 11

def diagonalLeft_0(cordinates_0, cordinates_X, i):
    cordinates_0[i] = cordinates_0[i] - 9

def eliminatingRight_0(cordinates_0, cordinates_X, i):
    cordinates_X.remove(cordinates_0[i] + 11)                   
    cordinates_0[i] = cordinates_0[i] + 11
    
def eliminatingLeft_0(cordinates_0, cordinates_X, i):
    cordinates_X.remove(cordinates_0[i] -9)                   
    cordinates_0[i] = cordinates_0[i] - 9

def forward_X(cordinates_0, cordinates_X, i):
    cordinates_X[i] = cordinates_X[i] - 1

def diagonalRight_X(cordinates_0, cordinates_X, i):
    cordinates_X[i] = cordinates_X[i] - 11

def diagonalLeft_X(cordinates_0, cordinates_X, i):
    cordinates_X[i] = cordinates_X[i] + 9

def eliminatingRight_X(cordinates_0, cordinates_X, i):
    cordinates_0.remove(cordinates_X[i] - 11)                   
    cordinates_X[i] = cordinates_X[i] - 11

def eliminatingLeft_X(cordinates_0, cordinates_X, i):
    cordinates_0.remove(cordinates_X[i] + 9)                   
    cordinates_X[i] = cordinates_X[i] + 9

#Prints out the board
def board(cordinates_0, cordinates_X):
    board = [18, 28, 38, 48, 58, 68, 78, 88, 17, 27, 37, 47, 57, 67, 77, 87, 16, 26, 36, 46, 56, 66, 76, 86, 15, 25, 35, 45, 55, 65, 75, 85, 14, 24, 34, 44, 54, 64, 74, 84, 13, 23, 33, 43, 53, 63, 73, 83, 12, 22, 32, 42, 52, 62, 72, 82, 11, 21, 31, 41, 51, 61, 71, 81]
    for i  in range(0,len(board)):
        if board[i] in cordinates_0:
            board[i] = "0"
        elif board[i] in cordinates_X:
            board[i] = "X"
        else:
            board[i] = "_"
                
    print(board[0: 8])
    print(board[8: 16])
    print(board[16: 24])
    print(board[24: 32])
    print(board[32: 40])
    print(board[40: 48])
    print(board[48: 56])
    print(board[56: 64])
    print("--------------------------------------")

#Method that check's who wins if neither X or 0 can make moves, it goes by how many pieces they have left, if they have the same amount it's a stalemate
def Stalemate(cordinates_0, cordinates_X):
    if len(cordinates_0) == len(cordinates_X):
        print("Stalemate")
        return
    else:
        if len(cordinates_0) > len(cordinates_X):
            print("0 won!")
            return
        if len(cordinates_0) < len(cordinates_X):
            print("X won!")
            return

#Method that picks a random possible choice and also will control player movement in the future
def random_val(cordinates_0, cordinates_X, i, movechoices, step, humanchoice):
    if humanchoice:
        print("Which move would you like to make? (type in the move)")
        
        while True:
            for x in movechoices:
                print(x)
            humanchoiceinput = input()
            if humanchoiceinput in movechoices:
                for y in movechoices:
                    if humanchoiceinput == y:
                        movechoices[y](cordinates_0, cordinates_X, i)
                        board(cordinates_0, cordinates_X)
                break
            else:
                print("Invalid input, please choose a move by typing it's name.")

            
    else:
        random_talet = random.randrange(0, len(movechoices))
        #i: save the position that could be played
        i = step[random_talet]
        movechoices[random_talet](cordinates_0, cordinates_X, i)
        board(cordinates_0, cordinates_X)
    

def main():
    #Cordinates are notated by the x position and y poistion in one number up to 8 since that is the size of the proper Breakthough board
    cordinates_0 = [11, 21, 31, 41, 51, 61, 71, 81, 12, 22, 32, 42, 52, 62, 72, 82]
    cordinates_X = [18, 28, 38, 48, 58, 68, 78, 88, 17, 27, 37, 47, 57, 67, 77, 87]
    victoryCordinates_0 = [18, 28, 38, 48, 58, 68, 78, 88]
    victoryCordinates_X = [11, 21, 31, 41, 51, 61, 71, 81]
    possibleCordinates = [18, 28, 38, 48, 58, 68, 78, 88, 17, 27, 37, 47, 57, 67, 77, 87, 16, 26, 36, 46, 56, 66, 76, 86, 15, 25, 35, 45, 55, 65, 75, 85, 14, 24, 34, 44, 54, 64, 74, 84, 13, 23, 33, 43, 53, 63, 73, 83, 12, 22, 32, 42, 52, 62, 72, 82, 11, 21, 31, 41, 51, 61, 71, 81]
    global human
    print("Do you (human) want to play? (yes/no) (human play not yet functional)")
    while True:
        humaninput = input()
        if humaninput == "yes" or humaninput == "y":
            human = True
            break
        if humaninput == "no" or humaninput == "n":
            human = False
            break

        else: 
            print("Invalid input, valid input: yes, no, y, n")
    game(cordinates_0, cordinates_X, victoryCordinates_0, victoryCordinates_X, possibleCordinates)

main()


    


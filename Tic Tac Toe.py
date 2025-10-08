#!/usr/bin/env python
# coding: utf-8

# In[1]:


board = [' '] * 10
player1 = 'x'
player2 = 'o'

def printBoard(board):
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("-"*10)

def gamewin():
    if board[1]==board[2]==board[3] and board[1]!=' ':
        return True
    elif board[4]==board[5]==board[6] and board[4]!=' ':
        return True
    elif board[7]==board[8]==board[9] and board[7]!=' ':
        return True
    elif board[1]==board[4]==board[7] and board[1]!=' ':
        return True
    elif board[2]==board[5]==board[8] and board[2]!=' ':
        return True
    elif board[3]==board[6]==board[9] and board[3]!=' ':
        return True
    elif board[1]==board[5]==board[9] and board[1]!=' ':
        return True
    elif board[3]==board[5]==board[7] and board[3]!=' ':
        return True
    else:
        return False
    
def checkdraw():
    return all(cell != ' ' for cell in board[1:])   # board full

def checkpos(pos):
    return board[pos] == ' '

def insert(letter, pos):
    if checkpos(pos):
        board[pos] = letter
        printBoard(board)
        if gamewin():
            print(f"Player {letter} wins!")
            exit()
        elif checkdraw():
            print("Draw!")
            exit()
    else:
        print("Position already taken, try again.")

def player1():
    pos = int(input("Player 1 (x), enter position (1-9): "))
    insert('x', pos)

def player2():
    pos = int(input("Player 2 (o), enter position (1-9): "))
    insert('o', pos)

# Main loop
while True:
    printBoard(board)
    player1()
    if gamewin() or checkdraw():
        break
    player2()
    if gamewin() or checkdraw():
        break


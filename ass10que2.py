# Write a program to place the queens randomly in the chess board so that all the conditions
# are satisfied. Find the solutions to the problem.

import random

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False
    
    return True

def solve_n_queens(n):
    board = [-1] * n
    rows = list(range(n))
    random.shuffle(rows)
    
    def place_queen(row):
        if row == n:
            return True
        
        cols = list(range(n))
        random.shuffle(cols)
        
        for col in cols:
            if is_safe(board, row, col, n):
                board[row] = col
                if place_queen(row + 1):
                    return True
                board[row] = -1
        
        return False
    
    while not place_queen(0):
        random.shuffle(rows)
        board = [-1] * n
    
    return board

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ["."] * n
        line[board[row]] = "Q"
        print(" ".join(line))

n = 8
solution = solve_n_queens(n)
print("Solution:")
print_board(solution)





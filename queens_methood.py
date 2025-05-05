def show_board(board):
    for now in board:
        print("".join(row))
    print("/n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == "Q":
            return False
    i, j, = row, col
    while i >= 0 and i >= 0:
        if  board[i][j]== "Q":
            return False
        i -= 1
        j -= 1

     i, j, = row, col
    while i >= 0 and j < n:
        if  board[i][j]== "Q":
            return False
        i -= 1
        j += 1
    return True

def place_queen(board, row, n):
    if row == n:
        show_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            place_queen(board,row + 1, n)
            board[row][col] = '.'

def solve_n_queens(n): 
    board = [['.']* n for _ in range(n)]
    place_queen(board, 0 , n)

solve_n_queens(4)
def solve_sudoku(board, row, col):

    size_board = len(board)

    if board[row][col] != 0:
        if col < size_board - 1:
            solve_sudoku(board, row, col + 1)
        elif row < size_board - 1:
            solve_sudoku(board, row + 1, 0)
        else:
            print(board)
    else:
        for number in range(1, len(board) + 1):
            if is_possible(board, row, col, number):
                board[row][col] = number
                if col < size_board - 1:
                    solve_sudoku(board, row, col + 1)
                elif row < size_board - 1:
                    solve_sudoku(board, row + 1, 0)

        #if it is not possible to place a number we need to backtrack
        board[row][col] = 0



def is_possible(board, row, col, number):
    size_board = len(board)

    #check row
    for index_col in range(size_board):
        if board[row][index_col] == number:
            return False

    # check column
    for index_row in range(size_board):
        if board[index_row][col] == number:
            return False

    # check box, works for 3x3 board
    for box_index in range(size_board):
        box_row = (box_index % 3) + (row // 3) * 3
        box_col = (box_index // 3) + (col // 3) * 3

        if board[box_row][box_col] == number:
            return False

    return True


sudoku =   [[8, 1, 0, 0, 3, 0, 0, 2, 7],
            [0, 6, 2, 0, 5, 0, 0, 9, 0],
            [0, 7, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 6, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 4],
            [0, 0, 8, 0, 0, 5, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 2, 0, 0, 1, 0, 7, 5, 0],
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]

solve_sudoku(sudoku, 0, 0)
from tkinter import *

root = Tk()
root.geometry("500x500")
sudoku =   [[8, 1, 0, 0, 3, 0, 0, 2, 7],
            [0, 6, 2, 0, 5, 0, 0, 9, 0],
            [0, 7, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 6, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 4],
            [0, 0, 8, 0, 0, 5, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 2, 0, 0, 1, 0, 7, 5, 0],
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]

def sudoku_number(sudoku, row, col):
    return sudoku[row][col]

def name_var(row, col):
    return f"{row}, {col}"


squares = [
    [Label(root, textvariable=IntVar(value=sudoku_number(sudoku, y, x), name=name_var(y, x)))
            for x in range(9)]
            for y in range(9)
]


for rows in range(9):
    for cols in range(9):
        squares[rows][cols].grid(row=rows, column=cols)


def update(row, col, val):
    squares[row][col].setvar(name_var(row, col), val)
    root.update()


def solve_sudoku(board, row, col):
    size_board = len(board)

    if board[row][col] != 0:
        if col < size_board - 1:
            if solve_sudoku(board, row, col + 1):
                return True
        elif row < size_board - 1:
            if solve_sudoku(board, row + 1, 0):
                return True
        else:
            return True
    else:
        for number in range(1, len(board) + 1):
            if is_possible(board, row, col, number):
                board[row][col] = number
                update(row, col, number)
                if col < size_board - 1:
                    if solve_sudoku(board, row, col + 1):
                        return True
                    else:
                        board[row][col] = 0
                        update(row, col, board[row][col])
                elif row < size_board - 1:
                    if solve_sudoku(board, row + 1, 0):
                        return True
                    else:
                        board[row][col] = 0
                        update(row, col, board[row][col])
    return False

def is_possible(board, row, col, number):
    size_board = len(board)

    # check row
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

start_button = Button(root, text="Start", command=lambda: solve_sudoku(sudoku, 0, 0))
start_button.grid(row=10, column=0, padx=10)

root.mainloop()

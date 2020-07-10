from tkinter import *
root = Tk()
root.geometry("500x500")

sudoku = [1, 0, 3, 2, 0, 0, 9, 5, 0]


def name(index):
    return f"var{index}"

labels = [Label(root, textvariable=IntVar(name=name(index) , value=sudoku[index])) for index in range(9)]
for index in range(9):
    labels[index].grid(row=0, column=index)

def update(idx, val):
    labels[idx].setvar(name(idx), val)
    root.update()

def solve_row(arr, index):

    if index >= len(arr):
        print(arr)
        return True

    if arr[index] != 0:
        if solve_row(arr, index+1):
            update(index, arr[index])
            return True
    else:
        for num in range(1, 10):
            if num not in arr:
                arr[index] = num
                update(index, num)

                if solve_row(arr, index + 1):
                    return True
        arr[index] = 0
    return False
start = Button(root, command=lambda: solve_row(sudoku, 0), text="start")
start.grid(row=1, column=0)


updatebutton = Button(root, command=lambda: update(3, 5), text="update")
updatebutton.grid(row=2, column=0)

root.mainloop()

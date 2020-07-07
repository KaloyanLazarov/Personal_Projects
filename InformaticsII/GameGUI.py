from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from itertools import permutations

#The geometry of the game interface
root = Tk()
root.title("Cows and Bulls")
root.geometry("650x1000")
root.grid_columnconfigure(index=(0,1), weight=2)
root.grid_rowconfigure(index=1, weight=0)

#Styles used for texts 
style = font.Font(size="40")
style2 = font.Font(size="30")

#The welcome to the game label and...
welcome_label = Label(root, text="Welcome to Cows and Bulls", padx=30)
welcome_label.grid(row=0, column=0)
welcome_label["font"] = style

#And the start button
start_button = Button(root, text="Press to start", command=display)
start_button["font"] = style
start_button.grid(row=1, column=0, padx=105, pady=15)

#The secret number which the user needs to guess
secret_number = game.number_to_guess()


#The function
#dictionary to keep track of every turn
history_dict = {} # history_dict[list(history_dict.keys())[-1]] - access the list with bulls and cows ... list(history_dict.keys())[-1] - access the last number
#generates a list of all possible values, gets reduced throughout the game
set_of_possibles = [int(''.join(map(str, x))) for x in permutations(range(10), 4) if x[0] != 0]
#2D list used to keep the number of times a digit, in certain position, appeared in a number, which resulted in bulls
matrix = [[0 for _ in range(10)] for _ in range(10)]


#The function to play the game
turn = 1
write = StringVar()
def next_number():
    global turn

    if turn > 1:
        if int(list(history_dict.keys())[-1]) in set_of_possibles:
            #Remove the number which the use has guessed
            #so the Algorithm does not guess e number more than once
            set_of_possibles.remove(int(list(history_dict.keys())[-1]))

        #checks if we can bundle 2 numbers and exclude possibilities
        check_for_exclude = Algorithm.exclude(history_dict)

        if check_for_exclude:
            #More information in the DOCstring
            Algorithm.exclude_number(set_of_possibles, check_for_exclude)

        if (history_dict[list(history_dict.keys())[-1]][0] + history_dict[list(history_dict.keys())[-1]][1]) == 4:
            Algorithm.the_four_cows_case(set_of_possibles, list(history_dict.keys())[-1])
            Algorithm.add_for_cows(matrix, list(history_dict.keys())[-1])

        if history_dict[list(history_dict.keys())[-1]][1] > 0:
            Algorithm.add_for_bulls(matrix, list(history_dict.keys())[-1])
        elif history_dict[list(history_dict.keys())[-1]][0] == 0 and history_dict[list(history_dict.keys())[-1]][1] == 0:
            Algorithm.the_zero_case(set_of_possibles, list(history_dict.keys())[-1])
        else:
            # history_dict[list(history_dict.keys())[-1]][1] < 0:
            Algorithm.only_cows(set_of_possibles, list(history_dict.keys())[-1])
            Algorithm.add_for_cows(matrix, list(history_dict.keys())[-1])

    dynamic_remaining.set("Remaining numbers:\n" + str(len(set_of_possibles)))
    write.set(Algorithm.next_number(set_of_possibles, history_dict, matrix, turn))
    turn += 1

#Dynamic string variable, we need to update the total value of the ramining numbers every time the use guesses
dynamic_remaining = StringVar()
dynamic_remaining.set("Remaining numbers:\n" + str(len(set_of_possibles)))
def display():
    """Displays all the required buttons and information about the game.
        Called every time when the start button is clicked"""

    global secret_number
    global user_number

    # remove the first label and button from the grid system
    start_button.grid_forget()
    welcome_label.grid_forget()

    close_button = Button(root, text="Close", command=lambda :root.destroy(), padx=50, pady=7)
    close_button.grid(row=0, column=1) #,sticky="ew")
    close_button["font"] = style

    restart_button = Button(root, text="Restart", command=clear, padx=50, pady=7)
    restart_button.grid(row=0, column=0) #, sticky="ew")
    restart_button["font"] = style

    next_number_button = Button(root, text="Next Number", command=next_number, padx=20, pady=7)
    next_number_button.grid(row=1, column=0)  # , columnspan=2, sticky="ew")
    next_number_button["font"] = style

    number_label = Label(root, text=f"{secret_number}")
    number_label.grid(row=2, column=0)
    number_label["font"] = style

    remaining = Label(root, textvariable=dynamic_remaining)
    remaining.grid(row=1, column=1)
    remaining["font"] = style2

    user_number = Entry(root, width=30, textvariable=write)
    user_number.grid(row=2, column=1)


#BEGIN OF: Helper functions used in the display function.
def play(event):
    """Checks if the user has won the game
        if list_for_output[-1][2][1] ->
        -> [-1][2] grabs the last [cows, bulls], [1] -> grabs the bulls
        and checks if bulls == 4
        The function is called everytime the Enter key is pressed"""
    list_for_output.append(output())

    list_for_output[-1][0].grid(row=len(list_for_output) + 2, column=1)
    list_for_output[-1][1].grid(row=len(list_for_output) + 2, column=0)

    if list_for_output[-1][2][1] == 4:
        choice = messagebox.askquestion(title="You win", message="Do you want to play again?")
        if choice == "yes":
            clear()
        else:
            lambda : root.destroy()
root.bind('<Return>', play)


#We use a list to store the list of outputs generated throughout the game
list_for_output = []
def output():
    """Output takes care of the dynamics we need to keep track of during the game
        output_label -> we need create new label every time the use guesses a number
        user_number_label -> we need to create a label of the number they gussed
        output -> we return the number of cows and bulls as well to be used for background purposes"""
    output = game.compare(secret_number, user_number.get())
    history_dict[user_number.get()] = output

    output_label = Label(root, text=f"Cows: {output[0]}, Bulls: {output[1]}")
    output_label["font"] = style2

    user_number_label = Label(root, text=user_number.get())
    user_number_label["font"] = style2
    user_number.delete(0, "end")

    return [output_label, user_number_label, output]


#Clear function used to reset the game state
#Stopped working at some point, nobody knows when :(
def clear():
    for sl in root.grid_slaves():
        sl.destroy()
    dynamic_remaining.set("Remaining numbers:\n" + str(len(set_of_possibles)))
    display()
#END OF: Helper functions

root.mainloop()

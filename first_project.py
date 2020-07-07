from random import randint


def game():
    lucky_number = randint(1, 10)
    used_numbers = []
    chances = 3

    while chances > 0:
        try:
            player_guess = int(input("Give your best shot!"))

            if lucky_number == player_guess and player_guess in range(1, 11) and player_guess not in used_numbers:
                print("You win!")
                break
            elif lucky_number != player_guess and player_guess in range(1, 11) and player_guess not in used_numbers:
                if lucky_number > player_guess:
                    print("Your shot was too low")
                else:
                    print("Your shot was too high!")
                chances -= 1
                used_numbers.append(player_guess)
            else:
                print(f"Try with number between 1 and 10, which you have not already used! You have used {used_numbers}!")
        except ValueError:
            print("Please try with numbers between 1 and 10")

game()

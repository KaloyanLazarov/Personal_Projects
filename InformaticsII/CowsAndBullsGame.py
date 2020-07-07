from itertools import permutations
import random


def number_to_guess():
    """Generates random 4 digit number with no repeating digits for the user to guess"""
    permutations_number = [int(''.join(map(str, x))) for x in permutations(range(10), 4) if x[0] != 0 ]
    return random.choice(permutations_number)


def compare(game_num, user_num):
    """Compares the two numbers and returns a list with the number of
        cows at the first index and the number of bulls at the 2nd"""
    game_num_lst = [x for x in list(str(game_num))]
    user_num_lst = [x for x in str(user_num)]
    bulls = 0
    cows = 0

    for  digit_idx in range(0, len(user_num_lst)): # we grab each digit from the number, which the user has guessed
        if game_num_lst[digit_idx] == user_num_lst[digit_idx]:
            bulls+=1

        for iter_idx in range(0, len(user_num_lst)):
            if digit_idx == iter_idx:
                # we skip when digit_idx = iter_idx because if user_num[digit_idx] == game_num[iter_idx] we have a bull
                continue
            if user_num_lst[digit_idx] == game_num_lst[iter_idx]:
                # with the number we have grabbed, we iterate over to check for equality
                cows += 1
    return [cows, bulls]

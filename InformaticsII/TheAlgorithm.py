from itertools import permutations
import random


#Functions used to add number to the matrix when we have bulls and cows
def only_cows(p_set, number): 
    p_set[:] = [x for x in p_set if str(x)[0] != str(number)[0]
            and str(x)[1] != str(number)[1]
            and str(x)[2] != str(number)[2]
            and str(x)[3] != str(number)[3]]

def add_for_bulls(matrix, number):
    """Access the matrix at the coresponding index and adds the value 3 ->
    the number 1234 has returned 1 bull, so we access the following idexes ->
    matrix[0][1] and we add 3 there -> marks that, at the first position,idexed [0]
    the number 1, indexed [1], appeared in number, which resulted bulls > 0"""
    row = 0
    for num in str(number):
        matrix[row][int(num)] += 3
        row+=1

def add_for_cows(matrix, number):
    """Called when we have cows only. Adds +=1 to the other positions.
    We know the digit is right, but it is not in the right place"""
    for num in str(number):
        for row_idx in str(number):
            if num == row_idx:
                continue
            matrix[int(row_idx)][int(num)] += 1


#Functions used to filter the set of remaining numbers
def only_cows(p_set, number):
    """If we got cows only -> we exclude all numbers which digits, at given position,
     are the same as the guessed number. Example:
     1234 = 2 cows => the secret number does not begin with 1, nor its second digit is 2 and so on"""
    p_set[:] = [remaining_number for remaining_number in p_set if
                str(remaining_number)[0] != str(number)[0] and
                str(remaining_number)[1] != str(number)[1] and
                str(remaining_number)[2] != str(number)[2] and
                str(remaining_number)[3] != str(number)[3]]


def the_four_sum(p_set, number):
    """When cows + bulls == 4 -> we know the digits,
    the secret number if a different permutation of them"""
    p_set[:] = [x for x in p_set if sorted(list(str(x))) == sorted(list(str(number)))]


def the_zero_sum(p_set, number):
    """When cows + bulls == 0, none of the digits are part of the secret_number,
    thus the intersection between the remaining_number and the number is 0"""
    p_set[:] = [x for x in p_set if len(set(str(x)).intersection(set(str(number)))) == 0]


def exclude(history_dict):
    """The function bundles the last guessed number with all previous guesses and stores it in current_set
    sum_current_set checks if the number of cows and bulls of those 2 numbers is 4, if so we can conclude that:
    the 4 digits of the secret number are among the 8 digits of the guessed numbers, thus excluding the 2 left digits"""

    for i in range(len(list(history_dict.keys())) - 1):
        current_set = set(list(str(list(history_dict.keys())[i]) +
                               str(list(history_dict.keys())[-1])))
        sum_current_set = sum(history_dict[list(history_dict.keys())[i]]) + \
                          sum(history_dict[list(history_dict.keys())[-1]])

        if sum_current_set < 4:
            continue
        else:
            if len(current_set) == 8:
                #This list passes the 2 numbers which need to be excluded
                return [excluded for excluded in range(10) if str(excluded) not in current_set]


def exclude_number(p_set, list_to_exclude):
    """Called when we have successfully bundled 2 numbers together.
    Maps the 2 numbers into strings and filters all numbers which include one or the other"""
    p_set[:] = [number for number in p_set if "".join(map(str, list_to_exclude))[0] not in str(number)
                and "".join(map(str, list_to_exclude))[1] not in str(number)]


#Functions used to determine the next next number
def next_number(p_set, history_dict, matrix, turn):
    """This function is used to determine the next number which the algorithm is going to guess"""
    if turn == 1:
        return random.choice(p_set)

    if turn == 2 and (sum(history_dict[list(history_dict.keys())[0]]) != 4):
        for number in p_set:
            if len(set(str(number)).intersection(set(str(list(history_dict.keys())[0])))) == 0:
                #Here, the algorithm might return None if the first guess excludes all such numbers
                #so the if statement above is never true
                return number
    else:
        if sum_matrix(matrix) < 200 and len(p_set) > 250:
            return grade_number(p_set, history_dict)
        else:
            return look_at_bulls(p_set, matrix)


def grade_number(all_possibles, history_dict):
    """Used to grade the remainnig numbers in the set. The idea is simple:
    find the number, which has the least common digits with the previously guessed number.
    The empowers our exclude function
    A heuristic to grade the numbers can be used here as well"""

    closest_number = 0 #list(history_dict.keys())[-1]
    sum_of_closest_number = -1
    for already_guessed in list(history_dict.keys()):
        if sum(history_dict[already_guessed]) > sum_of_closest_number:
            sum_of_closest_number = sum(history_dict[already_guessed])
            closest_number = already_guessed

    furthest_number = 0
    best_intersection = 5
    best_previous_intersection = 5

    random.shuffle(all_possibles)
    for number in all_possibles:
        current_intersection = len(set(str(number)).intersection(set(str(closest_number))))
        previous_number_intersection = len(set(str(number)).intersection(set(str(list(history_dict.keys())[-1]))))

        if (current_intersection + previous_number_intersection) < (best_intersection + best_previous_intersection):
            best_intersection = current_intersection
            furthest_number = number
            best_previous_intersection = previous_number_intersection
    return furthest_number


def look_at_bulls(p_set, matrix):
    """Find the number which is the best candidate for being the secret number.
    Uses the matrix, which stores how many times a given digit, in a certain position appeared in a number,
    which number resulted in bulls > 0"""

    closest_number = 0
    closest_number_sum = -1

    random.shuffle(p_set)
    #we shuffle the set in order to significantly lower the chance of guessing numbers which differ by only 1 or 2 digits
    #this could be done much better by implementing some kind oh heuristic
    for number in p_set:
        current_sum = sum(
            matrix[int(str(number)[0])] +
            matrix[int(str(number)[1])] +
            matrix[int(str(number)[2])] +
            matrix[int(str(number)[3])])

        if current_sum > closest_number_sum:
            closest_number = number
            closest_number_sum = current_sum
    return closest_number
#End of functions used to determine the next number


def sum_matrix(matrix):
    return sum([sum(x) for x in matrix])

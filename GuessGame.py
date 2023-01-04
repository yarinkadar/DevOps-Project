from random import random, randrange


def generate_number(max_value):
    return randrange(max_value)


def get_guess_from_user():
    return int(input("Try to guess the number :"))


def compare_results(random_number, user_guess):
    if random_number == user_guess:
        print("correct")
    else:
        print("incorrect")
    return random_number == user_guess


def play(difficulty):
    random_number = generate_number(difficulty)
    user_guess = get_guess_from_user()
    return compare_results(random_number, user_guess)

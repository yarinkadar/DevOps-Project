from random import randrange
from time import sleep
import os


def generate_sequence(difficulty):
    input("Are you ready? Type any key to generate the number:")
    numberslist = []
    for num in range(difficulty):
        numberslist.append(randrange(1, 101))
    print(numberslist)
    sleep(0.7)
    os.system('cls')   # will not work with pycharm.
    print("\n" * 10)   # will work with pycharm.

    return numberslist


def get_list_from_user(difficulty):
    userslist = []
    for num in range(difficulty):
        userslist.append(int(input("Enter the numbers you remember: ")))
    return userslist


def is_list_equal(numberlist, userlist):
    if numberlist == userlist:
        print("correct")
    else:
        print("incorrect")
    return numberlist == userlist


def play1(difficulty):
    randomlist = generate_sequence(difficulty)
    userlist = get_list_from_user(difficulty)
    return is_list_equal(randomlist, userlist)

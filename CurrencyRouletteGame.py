from random import randrange
from currency_converter import CurrencyConverter
c = CurrencyConverter()


def get_money_interval(difficulty):
    crr = c.convert(1, 'USD', 'ILS')
    currency = float(crr)
    ilsnumber = randrange(1, 100)
    print(f"What is {ilsnumber} USD in Shekels?")
    guessed_number = get_guess_from_user()
    real_number_in_usd = ilsnumber * currency
    if (real_number_in_usd - (5 - difficulty)) < guessed_number < (real_number_in_usd + (5 - difficulty)):
        print(f"Good guess! The exact number is {real_number_in_usd}")
        return True
    else:
        print(f"You are wrong... The exact number is {real_number_in_usd}")
        return False


def get_guess_from_user():
    guess = float(input("what is your guess? "))
    return guess


def play2(difficulty):
    get_money_interval(difficulty)


from Live import load_game, welcome
from GuessGame import play
from MemoryGame import play1
from CurrencyRouletteGame import play2
from Score import add_score

name = input("What is your name? ")
print(welcome(name))
x = 1

while x == 1:
    gamenumbers = load_game()  # game difficulty is gamenumbers[0], game number is gamenumbers[1]
    if gamenumbers[1] == 2:
       state = play(gamenumbers[0])
       if state == True:
           add_score(gamenumbers[0])
    elif gamenumbers[1] == 1:
        state = play1(gamenumbers[0])
        if state == True:
            add_score(gamenumbers[0])
    elif gamenumbers[1] == 3:
        state = play2(gamenumbers[0])
        if state == True:
            add_score(gamenumbers[0])
    game_again = input("do you want to play again? y/n :")
    if game_again == "y":
        x = 1
    elif game_again == "n":
        x = 0

print("Thanks for playing")



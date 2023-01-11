import GuessGame
import MemoryGame
import CurrencyRouletteGame

def welcome():
    print("Hello, What is your name?")
    name = input()
    print('''\nHello {name} and welcome to the World of Games (WoG). 
    Here you can find many cool games to play.'''.format(name=name))


welcome()

def load_game():
    print('''\nPlease choose a game to play
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
       guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')
    game = 0
    difficult = -1
    while True:
        try:
            game = int(input())
            if 0 < game <= 3:
                break
            else:
                print("Wrong choice, Please try again")
        except ValueError:
            print("Must be a number")

    print('''Great chiose!\n
    Please choose game difficulty from 1 to 5:''')
    while True:
        try:
            difficult = int(input())
            if 0 < difficult <= 5:
                print("Amazing!")
                break
            else:
                print("Bad choice, Please try again")

        except ValueError:
            print("Must be a number")

    if game == 1:
        MemoryGame.play(difficult)
    if game == 2:
        GuessGame.play(difficult)
    if game == 3:
        CurrencyRouletteGame.play(difficult)




load_game()
import random

def generate_number(Difficulty):
    return random.randint(1, Difficulty)


def get_guess_from_user(Difficulty):
    while True:
        print("Please enter a number between 1 to {DifficultyStr}".format(DifficultyStr=str(Difficulty)))
        try:
            number = int(input())
            if 1 <= number <= Difficulty:
                return number
            else:
                print("Number not in range")
        except ValueError:
            print("Must enter a number")

def compare_results(user_number, secret_number):
    if secret_number == user_number:
        print("Won")
        return True
    else:
        print("Lost")
        return False

def play(Difficulty):
    secret_number = generate_number(Difficulty)
    user_number = get_guess_from_user(Difficulty)
    return compare_results(user_number, secret_number)








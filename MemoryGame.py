import random
from time import sleep
import os

def generate_sequence(Difficulty):
    return random.sample(range(1, 101), Difficulty)
numbers_list = []
sleep(0.7)
os.system('cls')


def get_list_from_user(Difficulty):
    while True:
        print("Let's see if you can guess the numbers that appeared (a comma must be used between numbers)")
        try:
            numbers_list = input().split(",")
            if len(numbers_list) != Difficulty:
                print("Length error")
            else:
                for i in range(len(numbers_list)):
                    numbers_list[i] = int(numbers_list[i])
                return numbers_list
        except ValueError:
            print("Must be a number")



def is_list_equal(numbers_list , generated_list):
    if numbers_list == generated_list:
        print("Won")
        return True
    else:
        print("Lost")
        return False


def play(Difficulty):
    generated_list = generate_sequence(Difficulty)
    print(str(generated_list))
    user_list = get_list_from_user(Difficulty)
    return is_list_equal(generated_list , user_list)
















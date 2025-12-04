#Python Number Guesing Game 

import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("python number guessing game")
print(f"please select a number between {lowest_num}and{highest_num}")

while is_running:

    guess = input("Enter your Guest:")

    if guess.isdigit():
        guess = int(guess)
        guesses+=1
    if guess < lowest_num or guess > highest_num:
         print("That number is out of range")
         print(f"please select a number between {lowest_num}and{highest_num}")
    elif guess < answer:
         print("Too low! Try again!")
    elif guess > answer:
        print("Too high! Try Again!")
    else:
        print(f"correct! The answer was {answer}")
        print(f"Number of guesses:{guesses}")
        is_running= False 

else:
        print("Invalid guess")
        print(f"please select a number between {lowest_num}and{highest_num}")
        


    



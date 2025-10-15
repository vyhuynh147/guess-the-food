import os
os.system('cls||clear')

import random 

print("Welcome to the Food Guessing Game!\n")

secret_food = ["Sushi", "noodle", "salad", "steak", "pasta", "chicken", "nuggets", "pancake"]
print(secret_food)

random.choice(secret_food)
play_again = True
while True: 
    print("Try to guess the food that I'm thinking of...")
    input(" Guess food: ")
    





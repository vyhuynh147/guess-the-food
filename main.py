import os
os.system('cls||clear')

import random 

play_again = True


print("Welcome to the Food Guessing Game!\n")

secret_food = ["Sushi", "noodle", "salad", "steak", "pasta", "chicken", "nuggets", "pancake"]
print(secret_food)
random.choice(secret_food)

while True: 
    print("Try to guess the food that I'm thinking of...")

    max_attempts = 3
    attempt = 0
    while attempt < max_attempts:
        guess = input("Enter your guess: ").lower().strip()
        attempt +=1
    if guess == secret_food:
        print(" Congratulation, You guessed right", attempt, "tries")
    else: 
        hint = secret_food[0]
        print(" Wrong, Try again!!! Hint: The letter food starts with",hint)
        if guess != secret_food: 
            print(" Sorry, The food was",secret_food)   

            play_again = input(" Do you want to play again? (yes or no)").lower().strip()
            if play_again != "yes":
                break
            print(" Thank you for playing Guess the Food!")






import os
import random 
os.system('cls||clear')


secret_food = ["sushi", "noodle", "salad", "steak", "pasta", "chicken", "fries", "nuggets", "pancake", "cookie"]


while True: 
    # random food
    food = random.choice(secret_food) 

    print("Welcome to the Food Guessing Game!\n")
    print("Try to guess the food that I'm thinking of...")
    print("Here is the foods you can guess:", secret_food)
# use attempt to 
    max_attempts = 3
    attempt = 0
    # check if user has used hint
    use_hint = False 

    while attempt < max_attempts:
        guess = input("Enter your guess: ").lower().strip()
        attempt +=1
        if guess == food:
            print(" Congratulations, You guessed right", attempt, "tries")
            break
        else: 
            print(" Wrong, Try again!!!")
        # if not use hint to ask if they want hint or not.
            if not use_hint:
                hint = input(" Do you want to use hint? (yes or no):")
                if hint == "yes":
                    print(" Hint: The food starts with",food[0])
                    use_hint = True

    if guess != food: 
        print(" Sorry, The food was",food)   

    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again != "yes":
        print("Thank you for playing Guess the Food!")
        break






# Number Guessing Game
import random
# Generate a random number between 1 and 100
secret_number = random.randint(1, 50)
print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 50.")
while True:
    # Take user's guess
    guess = int(input("Enter your guess: "))
    # Check the guess
    if guess < secret_number:
        print("Too Low! Try Again.") 
    elif guess > secret_number:
        print("Too High! Try Again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break   # Exit the loop when the guess is correct

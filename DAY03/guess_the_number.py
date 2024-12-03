import random

def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        # Get user input
        try:
            user_guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        attempts += 1
        
        # Check the guess
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break  # Exit the loop when the number is guessed

# Run the game
guess_the_number()
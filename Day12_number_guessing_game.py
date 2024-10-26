import random
logo = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
"""

def number_guessing_game():
    random_number = random.randint(1, 100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        attempts = 10
        print("You have 10 attempts remaining to guess the number.")
        while attempts > 0:
            guess = int(input("Make a guess: "))
            if guess == random_number:
                return f"You got it! The answer was {guess}"
            elif guess > random_number:
                attempts -= 1
                print("Too high.")
                if attempts == 0:
                    return "You've run out of guesses, you lose."
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif guess < random_number:
                attempts -= 1
                print("Too low.")
                if attempts == 0:
                    return "You've run out of guesses, you lose."
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")


    elif difficulty == "hard":
        attempts = 5
        print("You have 5 attempts remaining to guess the number.")
        while attempts > 0:
            guess = int(input("Make a guess: "))
            if guess == random_number:
                return f"You got it! The answer was {guess}"
            elif guess > random_number:
                attempts -= 1
                print("Too high.")
                if attempts == 0:
                    return "You've run out of guesses, you lose."
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif guess < random_number:
                attempts -= 1
                print("Too low.")
                if attempts == 0:
                    return "You've run out of guesses, you lose."
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")



print(number_guessing_game())
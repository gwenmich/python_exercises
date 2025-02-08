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
    attempts = choose_difficulty()
    guess = 0
    while guess != random_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_guess(guess, random_number, attempts)

        if attempts == 0:
            return "You've run out of guesses, you lose."
        elif guess != random_number:
            print("Guess again.")



def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        raise TypeError("Error - please type 'easy' or 'hard' to choose difficulty.")




def check_guess(guess, random_number, attempts):
    if guess > random_number:
        print("Too high.")
        return attempts - 1
    elif guess < random_number:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {guess}")






if __name__ == "__main__":
    print(number_guessing_game())
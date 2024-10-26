import random

word_list = ["aardvaark", "baboon", "camel"]

chosen_word = random.choice(word_list)

word_in_blanks = "".join("_" for x in chosen_word)

user_lives = 3

while user_lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        print("Correct")
    else:
        print("Wrong. You've lost one life.")
        user_lives -= 1



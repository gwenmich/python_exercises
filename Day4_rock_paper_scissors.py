# rock paper scissors game with computer
import random

def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_choice = int(input("Please choose 1 for rock, 2 for paper, 3 for scissors: "))
    pc = random.choice(choices)
    user = choices[user_choice - 1]
    print(f"You chose {user}")
    print(f"PC chose {pc}")

    if user == pc:
        return "Draw"
    elif (user == "paper" and pc == "rock") or (user == "rock" and pc == "scissors") or (
            user == "scissors" and pc == "paper"):
        return "Player wins!"
    else:
        return "PC wins!"


print(play_rock_paper_scissors())

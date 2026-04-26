import random

choices = ["stone", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    if user == computer:
        return "Draw"

    if (user == "stone" and computer == "scissors") or \
       (user == "paper" and computer == "stone") or \
       (user == "scissors" and computer == "paper"):
        return "You Win!"

    return "Computer Wins!"

def play_round():
    user = input("Enter stone / paper / scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        return

    computer = get_computer_choice()

    print(f"Computer chose: {computer}")

    result = decide_winner(user, computer)
    print(result)
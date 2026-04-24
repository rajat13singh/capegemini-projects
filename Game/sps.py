import random
def stone_paper_scissors():
    print("\n--- Stone Paper Scissors ---")
    choices = ["stone", "paper", "scissors"]
    user = input("Enter your choice (stone/paper/scissors): ").lower()
    if user not in choices:
        print("Invalid choice!")
        return
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if user == computer:
        print("Result: It's a Draw!")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You Win!")
    else:
        print("Result: Computer Wins!")
stone_paper_scissors()

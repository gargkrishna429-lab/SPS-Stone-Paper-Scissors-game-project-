from utils import get_computer_choice
from logic import decide_winner

def play_round():
    user_choice = input("Enter stone, paper, or scissors: ").lower()
    
    if user_choice not in ["stone", "paper", "scissors"]:
        print("Invalid choice!")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = decide_winner(user_choice, computer_choice)
    print(result)

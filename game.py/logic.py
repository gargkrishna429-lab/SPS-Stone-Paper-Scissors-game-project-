def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        return "Congratulations: You win!"
    else:
        return "Better luck next time: Computer wins!"

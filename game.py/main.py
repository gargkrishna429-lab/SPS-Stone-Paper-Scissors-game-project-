from game import play_round

def main():
    while True:
        print("\n--- Stone-Paper-Scissors Game ---")
        print("1. Play Game")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            play_round()
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()

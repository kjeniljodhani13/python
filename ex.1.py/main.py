from groupex import get_user_choice, get_computer_choice, decide_winner

def main():
    print("Welcome to Rock, Paper, Scissors game!")

    while True:
        
        user_choice = get_user_choice()
        
        if user_choice == 'exit':
            print("Thank you for playing! Goodbye!")
            break

        
        computer_choice = get_computer_choice()
        
      
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

      
        result = decide_winner(user_choice, computer_choice)
        if result == "exit":
            print("Thank you for playing! Goodbye!")
            break
        print(result)
        print("\n")

if __name__ == "__main__":
    main()

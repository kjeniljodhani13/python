
import random

def get_user_choice():
    
    choice = input("Enter your choice (rock, paper, scissors or exit to quit): ").lower()
    
    
    valid_choices = ['rock', 'paper', 'scissors', 'exit']
    while choice not in valid_choices:
        choice = input("Invalid choice. Please enter rock, paper, scissors, or exit: ").lower()
    
    
    return choice

def get_computer_choice():
    
    choices = ['rock', 'paper', 'scissors']
    
    
    return random.choice(choices)

def decide_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    elif user_choice == 'exit':
        return "exit"
    else:
        return "Computer wins!"


import random
from colorama import Fore

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"


user_score = 0
computer_score = 0
    
print(Fore.LIGHTWHITE_EX+"Welcome to Rock-Paper-Scissors Game!")
print(Fore.GREEN+"""
Winning Rules:
1. Paper vs Rock --> Paper
2. Rock vs Scissors --> Rock
3. Scissors vs Paper --> Scissors
""")
    
while True:
    print(Fore.MAGENTA+"Choices are: 'rock', 'paper', or 'scissors'.")
    user_choice = input("Your choice: ").lower()
        
    if user_choice not in ['rock', 'paper', 'scissors']:
        print(Fore.RED+"Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
        continue
        
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
        
    result = winner(user_choice, computer_choice)
    print(Fore.YELLOW+result)
        
    if 'win' in result:
        user_score += 1
    elif 'lose' in result:
        computer_score += 1
        
    print(f"\nYour score: {user_score} | Computer's score: {computer_score}")
        
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'no':
        print("Thanks for playing!")
        break

import random


def show_scores(comp_score, user_score):
    print(f'\n--- Current Scores ---')
    print(f'Computer: {comp_score} | You: {user_score}')
    print('----------------------\n')

game_options = ["rock", "paper", "scissors"] 

comp_score = 0
user_score = 0

while True:

    computer_choice = random.choice(game_options)
    
    user_input = input('Enter (Rock, Paper, Scissors) or "exit" to stop: ').strip().lower()

    if user_input == 'exit':
        print("Thanks for playing!")
        break

    if user_input not in game_options:
        print("Invalid input! Please try again.")
        continue

    print(f"Computer chose: {computer_choice}")


    if user_input == computer_choice:
        print("It's a tie! 🤝")
    

    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("You win! 🎉")
        user_score += 1
    
  
    else:
        print("You lost! 😢")
        comp_score += 1

  
    show_scores(comp_score, user_score)

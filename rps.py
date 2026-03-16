import random

def get_choices():
    choices = ['rock', 'paper', 'scissors']

    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    
    computer_choice = random.choice(choices)

    print(f'You chose {player_choice} and computer chose {computer_choice}')

    if player_choice == computer_choice:
        return 'Tie :)'
        
    elif player_choice == 'rock' and computer_choice == 'scissors':
        return 'Winner!!!!'

    elif player_choice == 'paper' and computer_choice == 'rock':
        return 'Winner!!!!'

    elif player_choice == 'scissors' and computer_choice == 'paper':
        return 'Winner!!!!'

    else:
        return 'You go dey alright'

results = get_choices()

print(results)
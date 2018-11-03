#!/usr/bin/python3

import random

def input_human_play(input=input):
    play = input('rock, paper or scissors? ')
    while not is_valid_play(play):
        play = input('rock, paper or scissors? ')
    
    return(play)


def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']


def generate_computer_play():
    return random.choice(['rock', 'paper', 'scissors'])


def eval_game(human, computer):
    if human == computer:
        return 'tie'
    elif human == 'rock' and computer == 'paper':
        return 'computer'
    elif human == 'rock' and computer == 'scissors':
        return 'human'
    elif human == 'paper' and computer == 'rock':
        return 'human'    
    elif human == 'paper' and computer == 'scissors':
        return 'computer'    
    elif human == 'scissors' and computer == 'rock':
        return 'computer'        
    elif human == 'scissors' and computer == 'paper':
        return 'human'
        
        
        
def main(input=input):
    # nacist tah hrace & zkontrolovat vstup
    human = input_human_play(input)
    
    # tah pocitace a vypsat
    computer = generate_computer_play()
    print("Computer:", computer)
    
    # vyhodnotit a vypsat vysledek
    game = eval_game(human, computer)
    if game == 'tie':
        print('It\'s a tie')
    else:
        print(f'{game} won')
    
if __name__ == "__main__":
    main()
    
    

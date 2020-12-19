import random

# Instead of typing whole word, just type number of value, ex: 1 for 'rock'
rock = {1: 'rock'}
paper = {2: 'paper'}
scissors = {3: 'scissors'}

# Counter for win, who get 10, wins
my_score = 0
computer_score = 0

# Infinite loop
while True:
    # User pick number from dictionary, to get the value
    user = int(input('Enter: 1 for ROCK, 2 for PAPER, 3 for SCISSORS: '))
    computer = random.choice(['rock', 'paper', 'scissors'])

    # Checking if guesses are the same
    if user == 1 and rock[1] == computer:
        print(f'You Both Chooses: {computer}')
    if user == 2 and paper[2] == computer:
        print(f'You Both Chooses: {computer}')
    if user == 3 and scissors[3] == computer:
        print(f'You Both Chooses: {computer}')

    # Comparing computer choise with 'scissors', and checking if is not equal to rock, because scissors are weaker than rock
    # Rest is the same logic
    if user == 1 and rock[1] != computer and computer == 'scissors':
        print(f'I Win! Me: {rock[1]}, Computer: {computer}')
        my_score = my_score + 1
        if my_score == 10:
            print(f'I WIN THE GAME! {my_score}:{computer_score}')
            break
    if user == 2 and paper[2] != computer and computer == 'rock':
        print(f'I win! Me: {paper[2]}, Computer: {computer}')
        my_score = my_score + 1
        if my_score == 10:
            print(f'I WIN THE GAME! {my_score}:{computer_score}')
            break
    if user == 3 and scissors[3] != computer and computer == 'paper':
        print(f'I Win! Me: {scissors[3]}, Computer: {computer}')
        my_score = my_score + 1
        if my_score == 10:
            print(f'I WIN THE GAME! {my_score}:{computer_score}')
            break

    # Comparing computer choise with 'paper', and checking if is not equal to rock, because paper is stronger than rock
    # Rest is the same logic
    if user == 1 and rock[1] != computer and computer == 'paper':
        print(f'I Lost. Me: {rock[1]}, Computer: {computer}')
        computer_score = computer_score + 1
        if computer_score == 10:
            print(f'COMPUTER WINS. {computer_score}:{my_score}')
            break
    if user == 2 and paper[2] != computer and computer == 'scissors':
        print(f'I lost. Me: {paper[2]}, Computer: {computer}')
        computer_score = computer_score + 1
        if computer_score == 10:
            print(f'COMPUTER WINS. {computer_score}:{my_score}')
            break
    if user == 3 and scissors[3] != computer and computer == 'rock':
        print(f'I Lost. Me: {scissors[3]}, Computer: {computer}')
        computer_score = computer_score + 1
        if computer_score == 10:
            print(f'COMPUTER WINS. {computer_score}:{my_score}')
            break
import random

print('This is a game of Rock, Paper, Scissors. Type R for Rock, P for Paper, and S for Scissors')

# Loops the the code
while True:
    user = input('What do you choose?: ').upper()  # Ensure the input is uppercase
    while user not in ['R', 'P', 'S']:
        print('Only "R", "P", "S"')
        user = input('What do you choose?: ').upper()

    # Map user input to actual choices
    if user == 'R':
        user = 'Rock'
    elif user == 'P':
        user = 'Paper'
    else:
        user = 'Scissors'

    # Randomizer to the bot
    bot = ['Rock', 'Paper', 'Scissors']
    botpick = random.choice(bot)

    print(f'You chose {user}, the bot chose {botpick}')

    # Determine winner
    if user == botpick:
        print('It\'s a tie!')
    elif (user == 'Rock' and botpick == 'Scissors') or \
         (user == 'Paper' and botpick == 'Rock') or \
         (user == 'Scissors' and botpick == 'Paper'):
        print('You win!')
    else:
        print('Bot wins!')

    # Ask if the user wants to play again
    play_again = input('Do you want to play again? (Y/N): ').upper()
    if play_again != 'Y':
        print('Thanks for playing!')
        break

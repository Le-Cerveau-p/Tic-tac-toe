# Logo Art
logo = '''
 _____ ___ ____    _____  _    ____    _____ ___  _____ 
|_   _|_ _/ ___|  |_   _|/ \\  / ___|  |_   _/ _ \\| ____|
  | |  | | |   _____| | / _ \\| |   _____| || | | |  _|  
  | |  | | |__|_____| |/ ___ \\ |__|_____| || |_| | |___ 
  |_| |___\\____|    |_/_/   \\_\\____|    |_| \\___/|_____|
'''

# Possible game values
game_combo = {'1': ' ',
              '2': ' ',
              '3': ' ',
              '4': ' ',
              '5': ' ',
              '6': ' ',
              '7': ' ',
              '8': ' ',
              '9': ' '}

# Art for game UI
pic = f'''  
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
'''


# Possible Winning combinations
winning_combo = [['1', '5', '9'],
                 ['1', '2', '3'],
                 ['1', '4', '7'],
                 ['2', '5', '8'],
                 ['3', '6', '9'],
                 ['3', '5', '7'],
                 ['4', '5', '6'],
                 ['7', '8', '9']]



def decide(question, options):
    '''
    function to pick item from list of options
    '''
    decision = ""
    while decision not in options:
        decision = input(question)
    return decision


# initialize game UI
print(logo)
print(pic)

game_on = True

print("Enter a number to play. 'X' plays first, then 'O'.")
next_ = 'X'
play_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'e']
x_ = []
y_ = []

# Game main loop
while game_on:
    # take in player position choice
    entry = decide(f"It's {next_}'s turn to play.", play_options)

    play_options.remove(entry) # remove entered position from available positions

    # update next player
    if next_ == 'X':
        x_ += entry
        game_combo[entry] = 'X'
        next_ = 'O'
    else:
        y_ += entry
        game_combo[entry] = 'O'
        next_ = 'X'

    # refresh game_pic
    game_pic = f'''  
     {game_combo['1']} | {game_combo['2']} | {game_combo['3']}
    -----------
     {game_combo['4']} | {game_combo['5']} | {game_combo['6']}
    -----------
     {game_combo['7']} | {game_combo['8']} | {game_combo['9']}
    '''

    # display game_pic
    print(game_pic)
    for combo in winning_combo: # check for winning combo
        check_x = all(item in x_ for item in combo)
        if check_x:
            print('X wins!')
            game_on = False
        check_y = all(item in y_ for item in combo)
        if check_y:
            print('Y wins!')
            game_on = False
    if len(play_options) == 1: # check for draw
        print('Draw')
        game_on = False

    # break game loop
    if entry == 'e':
        game_on = False

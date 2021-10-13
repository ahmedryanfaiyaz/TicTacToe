"""
date: 10/13/2021
author: Ahmed Ryan
"""

the_board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' ',
}

boardKeys = []

for key in the_board:
    boardKeys.append(key)


def print_board(_board):
    print(_board['7'] + '/' + _board['8'] + '/' + _board['9'])
    print('-+-+-')
    print(_board['4'] + '/' + _board['5'] + '/' + _board['6'])
    print('-+-+-')
    print(_board['1'] + '/' + _board['2'] + '/' + _board['3'])
    print('-+-+-')


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_board(the_board)
        print('It is turn of ' + turn + ' specify the place you want to go: ')
        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print('Sorry this cell location is filled. Please choose another one.')
            continue

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                print_board(the_board)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game!')
                break
            if the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                print_board(the_board)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game!')
                break
            if the_board['3'] == the_board['2'] == the_board['3'] != ' ':
                print_board(the_board)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game!')
                break
            if the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                print_board(the_board)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game!')
                break
            if the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                print_board(the_board)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game!')
                break
            if the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                print_board(the_board)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game!')
                break
            if the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                print_board(the_board)
                print('\nGame Over')
                print('Player ' + turn + ' won the game!\n')
                break
            if the_board['3'] == the_board['5'] == the_board['7'] != ' ':
                print_board(the_board)
                print('\nGame Over')
                print('Player ' + turn + ' won the game!\n')
                break

        if count == 9:
            print('\nGame Over\n')
            print('The game is tie!')

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input('Do you want to restart the game? (y/n)\n')

    if restart == 'y' or restart == 'Y':
        for _key in boardKeys:
            the_board[_key] = ' '
        game()
    else:
        exit()


if __name__ == "__main__":
    game()

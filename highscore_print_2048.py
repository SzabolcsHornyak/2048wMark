from highscore_2048 import *    
def highscore_print():
    #filename = 'highscore_2048_{}x{}.csv'.format(w,h)
    open_file = open('highscore_2048_3x3.csv', "r")
    hs = list(open_file.read().split(', '))
    open_file.close()
    print(hs)
    length = 22 #leghosszabb lehetséges név: 'Schunnasaft Kapitän'
    h_score_first_row =  ' _     _       _                            '
    h_score_second_row = '| |   (_)     | |                           '
    h_score_third_row =  '| |__  _  __ _| |__  ___  ___ ___  _ __ ___ '
    h_score_fourth_row = '|  _ \| |/ _  |  _ \\/ __|/ __/ _ \\|  __/ _ \\'
    h_score_fifth_row =  '| | | | | (_| | | | \__ \ (_| (_) | | |  __/'
    h_score_sixth_row =  '|_| |_|_|\__, |_| |_|___/\___\___/|_|  \___|'
    h_score_seventh_row ='          __/ |                             '
    h_score_eigth_row =  '         |___/                              '
    print(h_score_first_row + '\n' + h_score_second_row + '\n' + h_score_third_row + '\n' + h_score_fourth_row + '\n' + h_score_fifth_row + '\n' + h_score_sixth_row + '\n' + h_score_seventh_row + '\n' + h_score_eigth_row + '\n\n' + 'player name'.ljust(length, ' ') + 'score'.rjust(length, ' ') + '\n' + '-'*length*2)
    for i in range(0, 11):
        if i % 2 == 1:
            print('\n' + str(hs[i - 1]).ljust(length, ' ') + str(hs[i]).rjust(length, ' '))
highscore_print()
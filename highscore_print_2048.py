'''
22 karakterben maximálni a bevitelt
az import_listből dictet csinálni
rendezni a dictet value szerint
kinyomtatni a dictet a többi fossal együtt
'''
from operator import itemgetter
from highscore_2048 import *    
def highscore_print():
#imports data from .csv
    filename = 'highscore_2048_{}x{}.csv'.format(w,h)
    open_file = open('filename', "r")
    hs = list(open_file.read().split(', '))
    open_file.close()
    hs_dict = {}
    hs_dict = dict((hs[i], int(hs[i + 1])) for i in range(0, len(hs), 2))
    hs_dict = list(sorted(tuple(hs_dict.items()), key=itemgetter(1)))
    print(hs_dict)
    length = 22
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
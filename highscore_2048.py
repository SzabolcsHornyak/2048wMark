# highscore
import os.path
from highscore_print_2048 import *
def highscore(player_name, w, h, score):
    filename = 'highscore_2048_{}x{}.csv'.format(w, h)
    if os.path.isfile(filename):
        open_file = open(filename, "r+")
        hs = open_file.read()
        highscore_list = hs.split(', ')
        open_file.write(', ' + str(player_name) + ', ' + str(score))
    else:
        open_file = open(filename, "w")       
        open_file.write(str(player_name) + ', ' + str(score))
    open_file.close()
    open_file = open(filename, "w")
    open_file.write(str(player_name) + ', ' + str(score))
    open_file.close()
    highscore_print(filename)
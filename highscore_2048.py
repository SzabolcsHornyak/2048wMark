# highscore
import os.path
def highscore(h,w,score):
    filename = 'highscore_2048_{}x{}.csv'.format(w,h)
    if os.path.isfile(filename):
        open_file = open(filename, "r+")
        hs = open_file.read()
        highscore_list = hs.split(', ')
        player_name = (str(input('Write here your name: ')))
        open_file.write(', ' + str(player_name) + ', ' + str(score))
    else:
        open_file = open(filename, "w")
        player_name = (str(input('Write here your name: ')))        
        open_file.write(str(player_name) + ', ' + str(score))
    filename.close()
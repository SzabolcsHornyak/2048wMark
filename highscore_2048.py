# highscore
import os.path
def highscore():
    score = 666
    w = 9
    h = 3
    filename = 'highscore_2048_{}x{}.csv'.format(w,h)
    if os.path.isfile(filename):
        open_file = open(filename, "r+")
        hs = open_file.read()
        highscore_list = hs.split(', ')
        player_name = (str(input('Write here your name: ')))
        open_file.write(', ' + str(player_name) + ': ' + str(score))
    else:
        open_file = open(filename, "w")
        player_name = (str(input('Write here your name: ')))        
        open_file.write(str(player_name) + ', ' + str(score))
    open_file = open(filename, "r")
    hs = open_file.read()
    highscore_list = hs.split(', ')
    highscore_dict = {}
    for i in highscore_list:
        i = highscore_dict[i]
    print(highscore_dict)

highscore()
# highscore
def highscore():
    open_file = open("highscore_2048.csv", "r")
    highscore = open_file.read()
    highscore_list = highscore.split(', ')
    open_file.close()
    

    print(highscore_list)
highscore()
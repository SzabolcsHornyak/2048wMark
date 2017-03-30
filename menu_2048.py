from move_2048 import *
import os


def custom_size():
    '''
    Input custom size of matrix
    '''
    w = 5
    h = 5
    os.system('clear')
    print('2048 GAME\n')
    w_inp = input('Set width (min: 2 / max 10): ')
    try:
        w = int(w_inp)
        if w > 10:
            w = 10
        if w < 3:
            w = 3
        print ('Width will be: ' + str(w) + '\n')
    except ValueError:
        print ('You got the default value: ' + str(w) + '\n')

    h_inp = input('Set height (min: 2 / max 10): ')
    try:
        h = int(h_inp)
        if h > 10:
            h = 10
        if h < 3:
            h = 3
        print ('Height will be: ' + str(h))
    except ValueError:
        print ('You got the default value: ' + str(h) + '\n')
        input('\nPRESS ANY KEY TO CONTINUE')
    #set_hw(h, w)
    gen_matrix(h, w)


def choose_menu():
    '''
    Generate menu
    '''
    global h, w
    os.system('clear')
    print(" _____  _____    ___  _____")
    print("/ __  \|  _  |  /   ||  _  |")
    print("`' / /'| |/' | / /| | \ V / ")
    print("  / /  |  /| |/ /_| | / _ \ ")
    print("./ /___\ |_/ /\___  || |_| |")
    print("\_____/ \___/     |_/\_____/\n")
    print('(e)asy       6x6')
    print('(n)ormal     5x5')
    print('(h)ard       4x4')
    print('(i)mpossible 3x3\n')
    print('(c)ustom size\n')
    diff_in = input('Choose difficulty: ')
    if diff_in == 'e':
        gen_matrix(6, 6)

    if diff_in == 'n':
        gen_matrix(5, 5)

    if diff_in == 'h':
        gen_matrix(4, 4)

    if diff_in == 'i':
        gen_matrix(3, 3)

    if diff_in == 'c':
        custom_size()

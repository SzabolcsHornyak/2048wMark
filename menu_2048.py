from move_2048 import *
import os


def custom_size():
    w = 5
    h = 5
    os.system('clear')
    print('2048 GAME\n')
    w_inp = input('Set width: ')
    try:
        w = int(w_inp)
    except ValueError:
        print ('You got the default value: ' + str(w) + '\n')

    h_inp = input('Set height: ')
    try:
        h = int(h_inp)
    except ValueError:
        print ('You got the default value: ' + str(h) + '\n')
        input('\nPRESS ANY KEY TO CONTINUE')
    #set_hw(h, w)
    gen_matrix(h, w)


def choose_menu():
    global h, w
    os.system('clear')
    print('2048 GAME\n')
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

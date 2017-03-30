'''
--  Feldarabolás: Main / mozgatás & reset / highscore / kirajzolás / menü
-- Bugfix: Ha változás történik a mátrixban csak akkor adhat hozzá új értéket
-- Globális változók csökkentése
-- High score fileba elmentése, betöltése új highscore hozzá adása / Dedicated to Mark
-- Docstringsek készítése
- Ha marad időnk: HP game feature. Időre kell egy bizonyos pontot elérni.
'''
from menu_2048 import *
from move_2048 import *


# MAIN THREAD
choose_menu()

add_rand_number()
add_rand_number()
draw_matrix()

while True:
    '''
    bottom line and movement input
    '''
    print('')
    input_string = 'MOVE: w/a/s/d | EXIT: x | NEW GAME: n | YOUR CHOICE? '
    if (empty_mapping() < 1):
        if (isMerged() is False):
            input_string = 'EXIT: x | NEW GAME: n | YOUR CHOICE? '
    c = input(input_string)
    c = c.lower()
    if len(c) > 1:
        c = c[0]
        draw_matrix()
    if c == ('w'):
        movement('up')
    if c == ('s'):
        movement('down')
    if c == ('a'):
        movement('left')
    if c == ('d'):
        movement('right')
    if c == ('x'):
        break
    if c == ('n'):
        reset_matrix()
        choose_menu()
        add_rand_number()
        add_rand_number()
        draw_matrix()

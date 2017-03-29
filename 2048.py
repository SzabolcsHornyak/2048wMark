'''
- Feldarabolás: Main / mozgatás & reset / highscore / kirajzolás / menü
- Bugfix: Ha változás történik a mátrixban csak akkor adhat hozzá új értéket
- Globális változók csökkentése
- High score fileba elmentése, betöltése új highscore hozzá adása / Dedicated to Mark
- Docstringsek készítése
- Ha marad időnk: HP game feature. Időre kell egy bizonyos pontot elérni.
'''
##############################################################################

# 2048 another program menus
from menu_2048 import *
from move_2048 import *
#from highscore_2048 import *


# MAIN THREAD
choose_menu()

add_rand_number()
add_rand_number()
draw_matrix()

while True:
    print('')
    c = input('MOVE: w/a/s/d | EXIT: x | NEW GAME: n | YOUR CHOICE? ')
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
    else:
        pass  # draw_matrix()

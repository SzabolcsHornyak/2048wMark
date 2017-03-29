import os
from random import randint

empty_X = []
empty_Y = []
w = 5
h = 5
Matrix = [[0 for x in range(w)] for y in range(h)]
temp_array = [[0 for x in range(w)] for y in range(h)]
new_value_X = -1
new_value_Y = -1
points = 0


def set_hw(input_array):
    global h, w
    h = len(input_array)
    w = len(input_array[0])
    return h, w


def gen_matrix(iw, ih):
    global Matrix, temp_array
    Matrix = [[0 for x in range(iw)] for y in range(ih)]
    temp_array = [[0 for x in range(iw)] for y in range(ih)]
    set_hw(Matrix)


def movement(directon):
    global new_value_X
    globals()["move_" + directon]()
    globals()["merge_" + directon]()
    globals()["move_" + directon]()
    if (Matrix != temp_array):
        add_rand_number()
    else:
        new_value_X = -1

    draw_matrix()
    copy_matrix()


def copy_matrix():
    global temp_array, Matrix
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            temp_array[j][i] = Matrix[j][i]


def empty_mapping():
    del empty_X[:]
    del empty_Y[:]
    for hi in range(h):
        for wi in range(w):
            if Matrix[hi][wi] == 0:
                empty_X.append(wi)
                empty_Y.append(hi)
    return len(empty_X)


def add_rand_number():
    numbers = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    global new_value_X, new_value_Y
    if (empty_mapping() > 0):
        random_coord = randint(0, (len(empty_X) - 1))
        Matrix[empty_Y[random_coord]][empty_X[random_coord]] = numbers[randint(0, 1)]  # rand 2 or 4
        new_value_X = empty_X[random_coord]
        new_value_Y = empty_Y[random_coord]
    else:
        new_value_X = -1
        new_value_Y = -1


def reset_matrix():
    global points
    points = 0
    for hi in range(h):
        for wi in range(w):
            Matrix[hi][wi] = 0
            temp_array[hi][wi] = 0


def isMerged():
    b_merged = False
    for wi in range(w):
        for hi in range(h - 1):
            if (Matrix[hi][wi] == Matrix[hi + 1][wi]) and (Matrix[hi][wi] != 0) and (Matrix[hi + 1][wi] != 0):
                b_merged = True
    for hi in range(h):
        for wi in range(w - 1):
            if (Matrix[hi][wi] == Matrix[hi][wi + 1]) and (Matrix[hi][wi] != 0) and (Matrix[hi][wi + 1] != 0):
                b_merged = True
    return b_merged


def merge_left():
    global points
    for hi in range(h):
        temp_array = []
        for wi in range(w - 1):  # same value merge
            if (Matrix[hi][wi] == Matrix[hi][wi + 1]) and (Matrix[hi][wi] != 0) and (Matrix[hi][wi + 1] != 0):
                points += Matrix[hi][wi] * 2
                Matrix[hi][wi] = Matrix[hi][wi] * 2
                Matrix[hi][wi + 1] = 0


def move_left():
    for hi in range(h):
        temp_array = []
        for wi in range(w):  # check the numbers above zero and move it!
            if Matrix[hi][wi] > 0:
                temp_array.append(Matrix[hi][wi])
        for i in range((w - len(temp_array))):
            temp_array.append(0)
        for wi in range(w):
            Matrix[hi][wi] = temp_array[wi]


def merge_right():
    global points
    for hi in range(h):
        temp_array = []
        for wi in range(w):  # same value merge
            if (Matrix[hi][wi] == Matrix[hi][wi - 1]) and (Matrix[hi][wi] != 0) and (Matrix[hi][wi - 1] != 0):
                points += Matrix[hi][wi - 1] * 2
                Matrix[hi][wi - 1] = Matrix[hi][wi] * 2
                Matrix[hi][wi] = 0


def move_right():
    for hi in range(h):
        temp_array = []
        for wi in range(w):
            if Matrix[hi][wi] > 0:
                temp_array.append(Matrix[hi][wi])
        for i in range((w - len(temp_array))):
            temp_array.insert(0, 0)
        for wi in range(w):
            Matrix[hi][wi] = temp_array[wi]


def merge_down():
    global points
    for wi in range(w):
        temp_array = []
        for hi in range(h - 1):  # same value merge
            if (Matrix[hi][wi] == Matrix[hi + 1][wi]) and (Matrix[hi][wi] != 0) and (Matrix[hi + 1][wi] != 0):
                points += Matrix[hi][wi] * 2
                Matrix[hi + 1][wi] = Matrix[hi][wi] * 2
                Matrix[hi][wi] = 0


def move_down():
    for wi in range(w):
        temp_array = []
        for hi in range(h):
            if Matrix[hi][wi] > 0:
                temp_array.append(Matrix[hi][wi])
        for i in range((h - len(temp_array))):
            temp_array.insert(0, 0)
        for hi in range(h):
            Matrix[hi][wi] = temp_array[hi]


def merge_up():
    global points
    for wi in range(w):
        temp_array = []
        for hi in range(h - 1):  # same value merge
            if (Matrix[hi][wi] == Matrix[hi + 1][wi]) and (Matrix[hi][wi] != 0) and (Matrix[hi + 1][wi] != 0):
                points += Matrix[hi][wi] * 2
                Matrix[hi][wi] = Matrix[hi][wi] * 2
                Matrix[hi + 1][wi] = 0


def move_up():
    for wi in range(w):
        temp_array = []
        for hi in range(h):
            if Matrix[hi][wi] > 0:
                temp_array.append(Matrix[hi][wi])
        for i in range((h - len(temp_array))):
            temp_array.append(0)
        for hi in range(h):
            Matrix[hi][wi] = temp_array[hi]


def draw_matrix_lines():
    global new_value_Y, new_value_X
    char_long = 5
    for hi in range(h):
        matrix_line = ''
        matrix_empty_line = ''
        for wi in range(w):
            spaces = ' ' * (char_long + 1 - len(str(Matrix[hi][wi])))
            spaces_end = ' ' * char_long
            if Matrix[hi][wi] == 0:
                matrix_line += int_to_color(hi, wi) + spaces_end + '-' + spaces_end
            else:
                matrix_line += int_to_color(hi, wi) + spaces + str(Matrix[hi][wi]) + spaces_end
            matrix_empty_line += int_to_color(hi, wi) + spaces_end + ' ' + spaces_end + '\x1b[0m'
        print(matrix_empty_line)
        print(matrix_line + '\x1b[0m')
        print(matrix_empty_line)


def draw_matrix():
    os.system('clear')
    print('2048 GAME // Score: ' + str(points) + '\n')
    if (empty_mapping() > 0):
        draw_matrix_lines()
    else:
        if (isMerged() is False):
            draw_matrix_lines()
            print('')
            spaces = ' ' * 20
            print('\x1b[1;33;40m' + spaces * 2)
            print(' ' * 15 + 'GAME OVER!' + ' ' * 15)
            print(spaces * 2 + '\n\x1b[0m')
        else:
            draw_matrix_lines()


def int_to_color(iy, ix):
    global new_value_X, new_value_Y
    icolor = Matrix[iy][ix]
    ret_color = '\x1b[0;30;47m'
    if icolor == 0:
        ret_color = '\x1b[1;30;47m'
    if icolor == 2:
        ret_color = '\x1b[1;36;40m'
    if icolor == 4:
        ret_color = '\x1b[1;35;40m'
    if icolor == 8:
        ret_color = '\x1b[1;34;40m'
    if icolor == 16:
        ret_color = '\x1b[1;33;40m'
    if icolor == 32:
        ret_color = '\x1b[1;32;40m'
    if icolor == 64:
        ret_color = '\x1b[1;31;40m'
    if icolor == 128:
        ret_color = '\x1b[1;31;40m'
    if icolor == 256:
        ret_color = '\x1b[1;31;40m'
    if icolor == 512:
        ret_color = '\x1b[1;31;40m'
    if icolor == 1024:
        ret_color = '\x1b[1;31;40m'
    if icolor == 2048:
        ret_color = '\x1b[1;31;40m'
    if icolor == 4096:
        ret_color = '\x1b[1;31;40m'
    if icolor == 8192:
        ret_color = '\x1b[1;31;40m'

    if iy == new_value_Y and ix == new_value_X:
        ret_color = '\x1b[0;30;43m'

    return ret_color

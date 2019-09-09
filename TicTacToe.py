val = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
xl = []
ol = []
Xor0 = 2
win_nums = ([1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 5, 9],
            [3, 5, 7],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9])


def ask_num():
    while True:
        position = input('Num from 1 to 9 ')
        if check_input_num(position):
            break
        else:
            continue
    return int(position)


def check_input_num(p):
    try:
        num = int(p)
    except ValueError:
        return False
    if num not in range(1, 10):
        return False
    else:
        return True


def already_added(position):
    used_num = position in xl or position in ol
    if used_num:
        print("This cell used, you lost turn")
    return used_num


def add_values(player, l, position=None):
    if not already_added(position):
        val[position] = player
        l.append(position)

        print('+++', player, l)


def check_win(l):
    win = False
    for each in win_nums:
        s1 = set(each)
        s2 = set(l)
        if s2.issuperset(s1):
            win = True
            print('You have won the GAME')
            break
    return win


def move_available(l):
    return ' ' in l


while True:

    position = ask_num()

    if Xor0 % 2 == 0:
        PLAYER = 'X'
        add_values(PLAYER, xl, position)
        won = check_win(xl)
    else:
        PLAYER = 'O'
        add_values(PLAYER, ol, position)
        won = check_win(ol)

    gboard = '''
                -{1}-|-{2}-|-{3}-
                ---+---+---
                -{4}-|-{5}-|-{6}-
                ---+---+---
                -{7}-|-{8}-|-{9}-
                '''.format(*val)

    print(gboard)
    Xor0 += 1

    if not move_available(val) or won:
        break

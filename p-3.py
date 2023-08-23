gameL = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def play(mapper, move_name):
    if move_name == 'x':
        Play = int(input("x? "))
    elif move_name == 'o':
        Play = int(input("o? "))

    c = 0
    for i in range(len(mapper)):
        for j in range(len(mapper)):
            c += 1
            if c == Play and mapper[i][j] == '-':
                mapper[i][j] = move_name
                return
            elif c == Play and mapper[i][j] != '-':
                print('try again')
                play(mapper, move_name)


def check(mapper, win_count=3):

    # >>> row <<<
    for i in mapper:
        save_row = ""
        count = 0
        for j in i:
            if j == save_row:
                count += 1
            else:
                save_row = j
                count = 1
            if count == win_count and save_row != '-':
                return save_row + ' won'

    # >>> column <<<
    for i in range(len(mapper)):
        save_column = ""
        count = 0

        for j in range(len(mapper)):
            if mapper[j][i] == save_column:
                count += 1
            else:
                save_column = mapper[j][i]
                count = 1
            if count == win_count and save_column != '-':
                return save_column + ' won'

    # >>> diameter <<<
    save_diameter = ""
    count = 0
    for i in range(len(mapper)):

        if mapper[i][i] == save_diameter:
            count += 1
        else:
            save_diameter = mapper[i][i]
            count = 1
        if count == win_count and save_diameter != '-':
            return save_diameter + ' won'

    save_diameter2 = ""
    count = 0
    for i in range(len(mapper)):
        if mapper[i][len(mapper) - 1 - i] == save_diameter2:
            count += 1
        else:
            count = 1
            save_diameter2 = mapper[i][len(mapper) - 1 - i]
        if count == win_count and save_diameter2 != '-':
            return save_diameter2 + ' won'


def show(mapper):
    game_show_s = ""
    for i in mapper:
        for j in i:
            game_show_s += j + '\t'
        game_show_s += '\n'
    return game_show_s


def istie(mapper):
    count = 0
    for i in mapper:
        for j in i:
            if j != '-':
                count += 1
    if count == (len(mapper))**2:
        return False


def Game(mapper):
    move = 'x'
    playing = True
    while playing:
        if move == 'x':
            move = 'o'
        elif move == 'o':
            move = 'x'

        play(mapper, move)
        print(show(mapper))

        res = check(mapper)
        if res == move + ' won':
            playing = False
        if res:
            print(res)
        if istie(mapper) == False:
            print('tie')
            playing = False
        else:
            print('keep playing')


Game(gameL)

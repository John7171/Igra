def header ():
    print("  КРЕСТИКИ-НОЛИКИ  ")
    print("___________________")
    print(" ввод в поле: a b ")
    print(" a - № строки,b - № столбца  ")

def view ():
    print()
    print("    | 0 | 1 | 2 | ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
    print()

def ask():
    while True:
        cords = input("       Ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        a, b = cords

        if not (a.isdigit()) or not (b.isdigit()):
            print(" Введите число! ")
            continue

        a, b = int(a), int(b)

        if a < 0 or a > 2 or b < 0 or b > 2:
            print("  Вне диапазона! ")
            continue

        if field[a][b] != " ":
            print(" Клетка занята! ")
            continue

        return a, b


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("    | 0 | 1 | 2 | ")
            for i, row in enumerate(field):
                row_str = f"  {i} | {' | '.join(row)} | "
                print(row_str)
            print("Выиграл X!!!")

            return True
        if symbols == ["0", "0", "0"]:
            print("    | 0 | 1 | 2 | ")
            for i, row in enumerate(field):
                row_str = f"  {i} | {' | '.join(row)} | "
                print(row_str)
            print("Выиграл 0!!!")
            return True
    return False


header ()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    view ()
    if count % 2 == 1:
        print(" Ход крестика")
    else:
        print(" Ход нолика")

    a, b = ask()

    if count % 2 == 1:
        field[a][b] = "X"
    else:
        field[a][b] = "0"

    if check_win():
        break

    if count == 9:
        print("    | 0 | 1 | 2 | ")
        for i, row in enumerate(field):
            row_str = f"  {i} | {' | '.join(row)} | "
            print(row_str)
        print(" Победила дружба!")
        break
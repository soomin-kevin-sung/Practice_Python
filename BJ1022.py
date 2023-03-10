import sys

board = []
nor, noc = 0, 0


def main(input=sys.stdin, output=sys.stdout):
    global board, nor, noc

    r1, c1, r2, c2 = map(int, input.readline().split())

    nor = r2 - r1 + 1
    noc = c2 - c1 + 1

    board = [[0 for _ in range(noc)] for _ in range(nor)]

    max_number = 0

    for i in range(nor):
        for j in range(noc):
            board[i][j] = get_number(r1 + i, c1 + j)
            max_number = max(max_number, board[i][j])

    num_of_digit = len(str(max_number))

    for row in board:
        for cell in row:
            output.write(f'{cell:{num_of_digit}} ')
        output.write('\n')


def get_number(r, c):
    global board, nor, noc

    level = max(abs(r), abs(c))
    br = (1 + level * 2) ** 2
    d = get_direction(r, c, level)
    cd = [1, 1, -1, -1]

    if d % 2 == 0:
        return br - (2 * level * d) - abs(level * cd[d] - c)
    else:
        return br - (2 * level * d) - abs(level * cd[d] - r)


def get_direction(r, c, level):
    # bottom
    if r == level:
        return 0
    # left
    elif c == -level:
        return 1
    # top
    elif r == -level:
        return 2
    # right
    else:
        return 3


if __name__ == '__main__':
    main()

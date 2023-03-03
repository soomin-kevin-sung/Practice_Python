import sys

# 푸는중

board = []


def main(input=sys.stdin, output=sys.stdout):
    global board

    r1, c1, r2, c2 = map(int, input.readline().split())

    nor = r2 - r1 + 1
    noc = c2 - c1 + 1

    board = [[0 for _ in range(noc)] for _ in range(nor)]

    cnt = 0
    d = [[0, 1], [-1, 0], [0, -1], [1, 0]]

    r = -r1
    c = -c1

    n = 1
    di = 0
    step = 0
    len_of_side = 1

    while cnt < nor * noc:
        cnt += set_number(r, c, n)
        n += 1
        step += 1

        if step == len_of_side:
            if di == 0:
                r, c = r + d[di][0], c + d[di][1]
                cnt += set_number(r, c, n)
                n += 1
                step = 2

                len_of_side += 2
            else:
                step = 1

            di = (di + 1) % 4

        r, c = r + d[di][0], c + d[di][1]

    for row in board:
        for cell in row:
            output.write(f'{cell:2} ')
        output.write('\n')


def set_number(r, c, num):
    global board

    if 0 <= r < len(board) and 0 <= c < len(board[r]):
        board[r][c] = num
        return 1

    return 0


if __name__ == '__main__':
    main()

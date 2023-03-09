import sys

board = []
nor, noc = 0, 0


def main(input=sys.stdin, output=sys.stdout):
    global board, nor, noc

    r1, c1, r2, c2 = map(int, input.readline().split())

    nor = r2 - r1 + 1
    noc = c2 - c1 + 1

    board = [[0 for _ in range(noc)] for _ in range(nor)]
    startpoint, num = get_arguments(r1, c1, r2, c2)
    total_count = nor * noc

    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    r = startpoint[0] - r1
    c = startpoint[1] - c1

    d = 0
    cnt = 1
    dcnt = startpoint[1] * 2

    if num == 1:
        d = 3
        cnt = 0
        dcnt = 1

    total_count = nor * noc
    while total_count > 0:
        if set_number(r, c, num):
            total_count -= 1

        num += 1
        cnt += 1

        if cnt == dcnt:
            cnt = 0
            d = (d + 1) % 4

            if d == 0:
                dcnt += 1

        r += dr[d]
        c += dc[d]




    # for row in board:
    #     for cell in row:
    #         output.write(f'{cell:2} ')
    #     output.write('\n')


def get_arguments(r1, c1, r2, c2):
    abs_geo = [abs(r1), abs(c1), abs(r2), abs(c2)]
    minpoint = min(abs_geo)

    if minpoint == 0:
        startpoint = (0, 0)
        num = 1
    else:
        startpoint = (minpoint - 1, minpoint)
        num = (1 + (minpoint - 1) * 2) ** 2

    return startpoint, num


def set_number(r, c, n):
    global board, nor, noc

    if 0 <= r < nor and 0 <= c < noc:
        board[r][c] = n
        return True

    return False


if __name__ == '__main__':
    main()

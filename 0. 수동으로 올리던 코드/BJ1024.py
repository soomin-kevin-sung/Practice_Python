import sys


def main(input=sys.stdin, output=sys.stdout):
    n, l = map(int, input.readline().split())

    ans = None
    for i in range(l, 101):
        # 2x + i - i = 2N / i
        x = (((2 * n) / i) - (i - 1)) / 2

        if x >= 0 and x % 1 == 0:
            ans = (int(x), i)
            break

    if ans is not None:
        for e in range(ans[0], ans[0] + ans[1]):
            output.write(f'{e} ')
    else:
        output.write('-1')


if __name__ == '__main__':
    main()

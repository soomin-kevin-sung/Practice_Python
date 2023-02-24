import sys


def main(input=sys.stdin, output=sys.stdout):
    n, k = map(int, input.readline().split())

    v = []
    for i in range(n):
        v.append(int(input.readline()))

    ans = []
    c = 0
    for i in range(1, n + 1):
        if v[-i] <= k:
            c += k // v[-i]
            k %= v[-i]

        if k == 0:
            break

    output.write(f'{c}')


if __name__ == '__main__':
    main()

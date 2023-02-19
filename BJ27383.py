import sys


def main(input=sys.stdin, output=sys.stdout):
    n, m = map(int, input.readline().split())

    a = []

    for i in range(n):
        a.append(list(map(int, input.readline().split())))

    for i in range(n):
        t = list(map(int, input.readline().split()))

        for j in range(m):
            output.write(f'{a[i][j] + t[j]} ')

        output.write('\n')


if __name__ == '__main__':
    main()

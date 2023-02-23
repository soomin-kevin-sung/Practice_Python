import sys


def main(input=sys.stdin, output=sys.stdout):
    n, k = map(int, input.readline().split())

    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
            if c == k:
                output.write(f'{i}')
                break

    if c != k:
        output.write(f'{0}')


if __name__ == '__main__':
    main()

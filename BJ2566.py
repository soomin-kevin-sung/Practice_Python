import sys


def main(input=sys.stdin, output=sys.stdout):
    maximum = -1
    x, y = -1, -1
    r = 1

    for _ in range(9):
        numbers = map(int, input.readline().split())

        c = 1
        for number in numbers:
            if maximum < number:
                maximum = number
                x = r
                y = c

            c += 1

        r += 1

    output.write(f'{maximum}\n')
    output.write(f'{x} {y}')


if __name__ == '__main__':
    main()

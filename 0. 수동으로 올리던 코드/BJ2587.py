import sys


def main(input=sys.stdin, output=sys.stdout):
    numbers = []

    for _ in range(5):
        numbers.append(int(input.readline()))

    numbers.sort()

    output.write(f'{sum(numbers) // 5}\n{numbers[2]}')


if __name__ == '__main__':
    main()

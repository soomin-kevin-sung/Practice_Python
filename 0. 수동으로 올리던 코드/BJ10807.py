import sys


def main(input=sys.stdin, output=sys.stdout):
    t = int(input.readline())
    nums = list(map(int, input.readline().split()))
    v = int(input.readline())

    cnt = [0 for _ in range(201)]
    for num in nums:
        cnt[num + 100] += 1

    output.write(f'{cnt[v + 100]}')


if __name__ == '__main__':
    main()

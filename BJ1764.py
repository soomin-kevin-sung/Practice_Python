import sys


def main(input=sys.stdin, output=sys.stdout):
    n, k = map(int, input.readline().split())

    d = {}
    for _ in range(n):
        name = input.readline().strip()
        d[name] = None

    ans = []
    for _ in range(k):
        name = input.readline().strip()
        if name in d:
            ans.append(name)

    ans.sort()
    output.write(f'{len(ans)}\n')
    for name in ans:
        output.write(f'{name}\n')


if __name__ == '__main__':
    main()

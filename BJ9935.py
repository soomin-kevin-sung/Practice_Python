import sys


def main(input=sys.stdin, output=sys.stdout):
    s = input.readline().strip()
    p = input.readline().strip()
    p = list(p)

    ans = []

    for c in s:
        ans.append(c)

        if ans[-1] == p[-1]:
            if ans[-len(p):] == p:
                del ans[-len(p):]

    output.write(''.join(ans) if ans else 'FRULA')


if __name__ == '__main__':
    main()

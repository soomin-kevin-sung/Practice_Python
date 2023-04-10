import sys


def is_palindrome(s, left, right):
    if left >= right:
        return 1, 1
    elif s[left] != s[right]:
        return 0, 1
    else:
        r, n = is_palindrome(s, left + 1, right - 1)
        return r, n + 1


def main(input=sys.stdin, output=sys.stdout):
    n = int(input.readline())

    for _ in range(n):
        s = input.readline().strip()
        res, noc = is_palindrome(s, 0, len(s) - 1)

        output.write(f'{res} {noc}\n')


if __name__ == '__main__':
    main()

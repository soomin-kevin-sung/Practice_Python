import sys
input = sys.stdin.readline


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False

    return True


while True:
    s = input().strip()
    if s == '0':
        break

    if is_palindrome(s):
        print('yes')
    else:
        print('no')

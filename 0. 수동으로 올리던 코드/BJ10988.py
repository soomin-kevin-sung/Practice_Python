def main():
    s = input()
    print(1 if is_palindrome(s) else 0)


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False

    return True


if __name__ == '__main__':
    main()

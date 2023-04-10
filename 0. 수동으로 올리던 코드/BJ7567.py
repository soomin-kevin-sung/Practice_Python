def main():
    s = input()

    result = 10
    for i in range(1, len(s)):
        result += 5 if s[i] == s[i - 1] else 10

    print(result)


if __name__ == '__main__':
    main()

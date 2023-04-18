def main():
    s = int(input())

    n = 1
    v = 0
    while v < s:
        v += n
        n += 1

    if v == s:
        print(n - 1)
    else:
        print(n - 2)


if __name__ == '__main__':
    main()

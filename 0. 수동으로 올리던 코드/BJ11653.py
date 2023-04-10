def main():
    n = m = int(input())

    i = 2
    while i < n:
        while not m % i:
            print(i)
            m //= i

        i += 1

    if m > 1:
        print(m)


if __name__ == '__main__':
    main()
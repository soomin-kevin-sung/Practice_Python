def main():
    h, m = map(int, input().split())
    n = (m + 15) % 60

    if m < n:
        print((h + 23) % 24, n)
    else:
        print(h, n)


if __name__ == '__main__':
    main()
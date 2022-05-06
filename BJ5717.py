def main():
    while True:
        m, f = map(int, input().split())

        if m == f == 0:
            break

        print(m + f)


if __name__ == '__main__':
    main()

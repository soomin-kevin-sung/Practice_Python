def main():
    y = int(input())

    if (not y % 4 and y % 100) or not y % 400:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()

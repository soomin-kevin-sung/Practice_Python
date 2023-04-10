def main():
    n = int(input())
    s = input()

    a_count = s.count('A')
    if n / 2 < a_count:
        print('A')
    elif n / 2 > a_count:
        print('B')
    else:
        print('Tie')


if __name__ == '__main__':
    main()

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        max_school_name = ''
        max_liter = -1
        for _ in range(n):
            school_name, liter = input().split()
            liter = int(liter)

            if max_liter < liter:
                max_school_name = school_name
                max_liter = liter

        print(max_school_name)


if __name__ == '__main__':
    main()
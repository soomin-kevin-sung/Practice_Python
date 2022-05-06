def main():
    t = int(input())
    q = [0 for _ in range(5)]

    for _ in range(t):
        x, y = map(int, input().split())

        if x > 0 and y > 0:
            q[1] += 1
        elif x < 0 and y > 0:
            q[2] += 1
        elif x < 0 and y < 0:
            q[3] += 1
        elif x > 0 and y < 0:
            q[4] += 1
        else:
            q[0] += 1

    print('Q1:', q[1])
    print('Q2:', q[2])
    print('Q3:', q[3])
    print('Q4:', q[4])
    print('AXIS:', q[0])


if __name__ == '__main__':
    main()

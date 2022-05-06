def main():
    t = int(input())

    for _ in range(t):
        score_y = 0
        score_k = 0

        for __ in range(9):
            y, k = map(int, input().split())
            score_y += y
            score_k += k

        if score_y > score_k:
            print('Yonsei')
        elif score_y < score_k:
            print('Korea')
        else:
            print('Draw')


if __name__ == '__main__':
    main()

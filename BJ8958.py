def main():
    t = int(input())

    for _ in range(t):
        s = input()

        score = 0
        result_score = 0

        for c in s:
            if c == 'O':
                score += 1
                result_score += score
            else:
                score = 0

        print(result_score)


if __name__ == '__main__':
    main()

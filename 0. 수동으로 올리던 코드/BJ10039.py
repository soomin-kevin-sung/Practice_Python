def main():
    sum_of_score = 0

    for _ in range(5):
        score = int(input())

        if score < 40:
            score = 40

        sum_of_score += score

    print(sum_of_score // 5)


if __name__ == '__main__':
    main()

def main():
    t = int(input())

    max_reward = 0

    for _ in range(t):
        a, b, c = sorted(map(int, input().split()))

        max_reward = max(max_reward, get_reward(a, b, c))

    print(max_reward)


def get_reward(score1, score2, score3):
    if score1 == score3:
        return 10000 + score1 * 1000
    elif score1 == score2 or score2 == score3:
        return 1000 + score2 * 100
    else:
        return max(score1, score2, score3) * 100


if __name__ == '__main__':
    main()

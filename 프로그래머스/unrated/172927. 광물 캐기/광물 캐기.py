tired = [
    [1, 1, 1],
    [5, 1, 1],
    [25, 5, 1]
]


def solution(picks, minerals):
    ans = 0
    cnts = []
    for i in range(0, len(minerals), 5):
        check_minerals = minerals[i:i + 5]
        cnt = get_minerals_count(check_minerals)
        cnts.append(cnt)

    num_of_picks = sum(picks)
    cnts = cnts[:num_of_picks]

    cnts.sort(reverse=True)
    cnt_idx = 0
    for pick_idx in range(3):
        while cnt_idx < len(cnts) and picks[pick_idx]:
            for mineral_idx in range(3):
                ans += cnts[cnt_idx][mineral_idx] * tired[pick_idx][mineral_idx]
            cnt_idx += 1
            picks[pick_idx] -= 1
    return ans


def get_minerals_count(minerals):
    idx = {'diamond': 0, 'iron': 1, 'stone': 2}
    ans = [0, 0, 0]
    for mineral in minerals:
        ans[idx[mineral]] += 1
    return ans

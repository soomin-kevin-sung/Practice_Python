import math

# 참고 : https://blog.naver.com/jjys9047/222572840898
# 해당 크레인들로 옮겨야하는 박스의 갯수 / 크레인의 갯수 = 시간

n = int(input())
crains = sorted(list(map(int, input().split())))
m = int(input())
boxes = sorted(list(map(int, input().split())))

if crains[-1] < boxes[-1]:
    print(-1)
else:
    # 크레인마다 필수적으로 옮겨야하는 박스를 카운팅하는 변수
    cnts = [0] * n
    crain_idx = 0
    box_idx = 0

    while crain_idx < n and box_idx < m:
        if boxes[box_idx] <= crains[crain_idx]:
            cnts[crain_idx] += 1
            box_idx += 1
        else:
            crain_idx += 1

    # 가장 높은 무게를 운용할 수 있는 크레인부터 검사
    cnts.reverse()

    ans = 0
    num_of_boxes = 0
    for i in range(n):
        num_of_boxes += cnts[i]
        ans = max(ans, math.ceil(num_of_boxes / (i + 1)))

    print(ans)

t = int(input())
while t:
    t -= 1
    li = list(map(int, input().split()))
    li.sort(reverse=True)

    print(li[2])

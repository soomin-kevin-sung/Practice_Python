n = int(input())
nums = list(map(int, input().split()))

nums.sort()

if n % 2:
    print(nums[(n // 2)])
else:
    print(nums[(n // 2) - 1])

nums = list(map(int, input().split()))
print(sum([i * i for i in nums]) % 10)

import sys

input = sys.stdin
output = sys.stdout

nums = list(map(int, list(input.readline().strip())))

sum_of_nums = 0
has_zero = False

for num in nums:
    if num == 0:
        has_zero = True

    sum_of_nums += num

if sum_of_nums % 3 or not has_zero:
    output.write(f'{-1}')
else:
    nums.sort(reverse=True)
    output.write(''.join(map(str, nums)))

import sys

input = sys.stdin
output = sys.stdout


def get_new_num(num_str, rep_char):
    tmp = ''

    for c in num_str:
        if c == '5' or c == '6':
            tmp += rep_char
        else:
            tmp += c

    return int(tmp)


a, b = input.readline().split()
min_num = get_new_num(a, '5') + get_new_num(b, '5')
max_num = get_new_num(a, '6') + get_new_num(b, '6')

output.write(f'{min_num} {max_num}')

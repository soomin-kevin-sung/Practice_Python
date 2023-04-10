import sys

sum_of_score = 0
sum_of_value = 0

grade_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0
}

for _ in range(20):
    subject, score, grade = sys.stdin.readline().split()

    if grade == 'P':
        continue

    score = float(score)
    grade_score = grade_dict[grade]
    sum_of_score += score
    sum_of_value += score * grade_dict[grade]

sys.stdout.write(f'{sum_of_value / sum_of_score:6f}')

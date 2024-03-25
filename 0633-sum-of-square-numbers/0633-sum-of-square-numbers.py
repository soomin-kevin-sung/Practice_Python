import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        b = int(math.sqrt(c))
        while b > 0:
            a = c - b ** 2
            if math.sqrt(a).is_integer():
                return True

            b -= 1

        return False
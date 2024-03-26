class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        m = 0
        for num in nums:
            if num <= 0:
                continue

            s.add(num)
            m = max(m, num)
            
        for i in range(1, m + 1):
            if i not in s:
                return i

        return m + 1
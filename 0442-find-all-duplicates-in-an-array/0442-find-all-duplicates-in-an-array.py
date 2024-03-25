class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        s = set()

        for num in nums:
            if num in s:
                ans.append(num)

            s.add(num)

        return ans
        
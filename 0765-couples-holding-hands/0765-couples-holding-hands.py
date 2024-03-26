class Solution:
    def minSwapsCouples(self, row):        
        cnt = 0
        for i in range(len(row) // 2):
            if row[i * 2] // 2 != row[i * 2 + 1] // 2:
                cnt += 1

        return max(0, cnt - 1)
            
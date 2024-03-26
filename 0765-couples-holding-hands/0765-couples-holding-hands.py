class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d = {}
        for i in range(len(row)):
            d[row[i]] = i

        # vis = set()
        cnt = 0
        for i in range(len(row) // 2):
            if row[i * 2] // 2 != row[i * 2 + 1] // 2:
                a = row[i * 2] // 2 * 2
                a = a if a != row[i * 2] else row[i * 2] // 2 * 2 + 1

                # 값 변경
                row[d[a]], row[i * 2 + 1] = row[i * 2 + 1], row[d[a]]

                # 위치 변경
                d[row[d[a]]] = d[a]
                d[a] = i * 2 + 1

                # 카운트
                cnt += 1

        return cnt
        
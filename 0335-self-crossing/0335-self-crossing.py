class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(3, len(distance)):
            if (
                distance[i] >= distance[i - 2] and
                distance[i - 1] <= distance[i - 3]
            ):
                return True

            if i == 4:
                if (
                    distance[i] >= distance[i - 2] - distance[i - 4] and
                    distance[i - 1] == distance[i - 3]
                ):
                    return True
            elif i > 4:
                d = distance[i - 2] - distance[i - 4]
                d = d if d >= 0 else distance[i - 2]
                flag = (
                    distance[i] <= distance[i - 2] and
                    distance[i] >= d
                )

                d = distance[i - 3] - distance[i - 5]
                d = d if d >= 0 else distance[i - 3]
                flag2 = (
                    distance[i - 1] <= distance[i - 3] and
                    distance[i - 1] >= d
                )

                if flag and flag2:
                    return True

        return False

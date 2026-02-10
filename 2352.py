from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0

        has = {}
        for i in range(len(grid)):
            has2 = []
            for j in range(len(grid)):
                has2.append((grid[j][i]))
                has[i] = has2

        for i in range(len(grid)):
            for j in range(len(grid)):
                if (grid[i]) == (has[j]):
                    count += 1
        return count

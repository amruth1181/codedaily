class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        zeros = 0
        best = 0

        for y in range(len(nums)):
            if nums[y] == 0:
                zeros += 1          # new element entered window → update count

            while zeros > k:        # window invalid → shrink from left
                if nums[i] == 0:
                    zeros -= 1      # leaving element was a zero → decrement
                i += 1

            best = max(best, y - i + 1)  # window is valid → update answer

        return best
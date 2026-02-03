class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        left = 0
        best = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, i - left + 1)
        return best - 1



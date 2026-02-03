class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        list1 = nums[::-1]
        lefts = [0] * len(nums)
        rights = [0] * len(nums)
        dum = 0
        dum2 = 0

        for i in range(1, len(nums)):
            dum += nums[i - 1]
            lefts[i] = dum
        for j in range(1, len(nums)):
            dum2 += list1[j - 1]
            rights[j] = dum2
        for z in range(len(nums)):
            if lefts[z] == rights[::-1][z]:
                return z

        return -1

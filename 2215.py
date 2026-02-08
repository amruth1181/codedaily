class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=[]
        b=[]
        ans=[]
        for i in nums1:
            if i not in nums2 and i not in a :
                a.append(i)

        ans.append(a)

        for j in nums2:
            if j not in nums1 and j not in b:
                b.append(j)

        ans.append(b)

        return ans


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1-s2), list(s2-s1)]
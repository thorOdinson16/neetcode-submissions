class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = set()
        for i in nums:
            if i in x:
                return i
            else:
                x.add(i)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        y = set(nums)
        if len(nums) == len(y):
            return False
        else:
            return True
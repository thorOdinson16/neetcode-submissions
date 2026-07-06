class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i,n in enumerate(nums):
            if (target - n in x):
                li = [x[target-n], i]
            else:
                x[n] = i
        return li
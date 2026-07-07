class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        y = 0
        x = 0
        for i in unique:
            x = 1
            if i-1 in unique:
                continue
            if len(unique) == 1:
                return 1
            if (i+1 in unique):
                curr = i
                while curr+1 in unique:
                    x += 1
                    curr += 1
            if y < x:
                y = x
            else:
                y = y
        return y
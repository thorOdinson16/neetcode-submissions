class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        y = 1
        left = []
        right = []
        final = []
        for i in range(len(nums)):
            if i==0:
                left.append(x)
                right.append(y)
                continue
            x *= nums[i-1]
            left.append(x)
            y *= nums[len(nums)-i]
            right.append(y)
        right.reverse()
        for i in range(len(nums)):
            final.append(left[i]*right[i])
        return final
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            prod = min(heights[i],heights[j])*(j-i)
            if prod > result:
                result = prod
            else:
                pass
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return result

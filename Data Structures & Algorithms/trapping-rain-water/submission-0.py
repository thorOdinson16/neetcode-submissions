class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        temp = deque()
        right = [0]*len(height)
        left.append(0)
        for i in range(len(height)-1):
            left.append(max(left[i], height[i]))
            right[len(height)-2-i] = max(right[len(height)-1-i], height[len(height)-1-i])
        water = 0
        for i in range(len(height)):
            if (min(left[i],right[i]) - height[i]) > 0:
                water += min(left[i],right[i]) - height[i]
        return water
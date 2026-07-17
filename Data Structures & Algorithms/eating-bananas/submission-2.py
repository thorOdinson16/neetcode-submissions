class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = (left + right)//2
            s = 0
            for i in piles:
                if i%mid == 0:
                    s = s + (i//mid)
                else:
                    s = s + ((i//mid) + 1)
            if s <= h:
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res
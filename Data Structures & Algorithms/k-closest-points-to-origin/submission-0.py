import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for i in points:
            x, y = i
            z = math.sqrt(x*x + y*y)
            heapq.heappush(heap, (z, i))
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans
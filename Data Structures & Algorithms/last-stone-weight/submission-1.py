import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x == y:
                continue
            else:
                if x < y:
                    z = x - y
                else:
                    z = y - x
                heapq.heappush(heap, z)
        if len(heap) == 0:
            return 0
        return -heap[0]
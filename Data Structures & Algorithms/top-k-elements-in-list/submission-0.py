from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        li = cnt.most_common(k)
        r = []
        for a,b in li:
            r.append(a)
        return r
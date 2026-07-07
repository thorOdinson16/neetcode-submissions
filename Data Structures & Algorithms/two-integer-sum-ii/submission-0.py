class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(numbers):
            d[n] = i+1
        for key,value in d.items():
            if target-key in d:
                if value < d[target-key]:
                    a = [value, d[target-key]]
        return a
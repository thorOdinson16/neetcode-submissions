class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        x = sorted(nums)
        for i in range(len(x)):
            j = i+1
            k = len(x)-1
            while j < k:
                if x[i]+x[j]+x[k] == 0:
                    t = (x[i],x[j],x[k])
                    if tuple(sorted(t)) in result:
                        pass
                    else:
                        result.add(tuple(sorted(t)))
                    j += 1
                    k -= 1
                elif (x[i]+x[j]+x[k]) < 0:
                    j += 1
                else:
                    k -= 1
        return list(result)
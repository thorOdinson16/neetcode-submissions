class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for i in strs:
            if tuple(sorted(i)) in x:
                x[tuple(sorted(i))].append(i)
            else:
                x[tuple(sorted(i))] = [i]
        return list(x.values())
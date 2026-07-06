class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(s)
        y = list(t)
        if sorted(x) == sorted(y):
            return True
        else:
            return False
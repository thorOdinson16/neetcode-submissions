class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        flag = False
        while right < len(s2):
            if sorted(s2[left:right+1:]) == sorted(s1):
                flag = True
                break
            else:
                left += 1
                right += 1
        return flag

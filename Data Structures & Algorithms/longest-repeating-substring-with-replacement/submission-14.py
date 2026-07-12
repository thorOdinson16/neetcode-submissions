class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        x = {}
        li = []
        for right in range(0,len(s)):
            if s[right] in x:
                x[s[right]] += 1
            else:
                x[s[right]] = 1
            if sum(x.values()) - max(x.values()) > k:
                li.append(sum(x.values())-1)
                x[s[left]] -= 1
                left += 1
        li.append(sum(x.values()))
        return(max(li))    

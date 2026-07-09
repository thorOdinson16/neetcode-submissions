class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        arr = [0]*len(s)
        x = set()
        x.add(s[0])
        arr[0] = 1
        left = 0
        for i in range(1, len(s)):
            if s[i] in x:
                arr[i] = arr[i-1]+1
                while s[i] in x:
                    x.remove(s[left])
                    left += 1
                arr[i] = i - left + 1
                x.add(s[i])
            else:
                arr[i] = arr[i-1]+1
                x.add(s[i])
        print(arr)
        return max(arr)
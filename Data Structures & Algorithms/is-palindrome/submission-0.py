class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(c for c in s if c.isalnum()).lower()
        r = clean_s[::-1]
        if r == clean_s:
            return True
        else:
            return False
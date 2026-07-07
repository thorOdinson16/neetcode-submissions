class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s+str(len(i))+"#"+i
        return s
    def decode(self, s: str) -> List[str]:
        i= 0
        a= []
        while i < len(s):
            j = i
            x=""
            while s[j] != '#':
                x = str(x)+str(s[j])
                j+=1
            x = int(x)
            i = j+1
            a.append(s[i:i+x])
            i += x
        return a

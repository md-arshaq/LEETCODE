class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        i=0
        j=1
        for j in range(1,len(s)):
            score = score + abs(ord(s[j])-ord(s[i]))
            i+=1
        return score
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        if len(s)==0:
            return True
        while(i<len(t)):
            if j==len(s):
                return True
            if s[j]==t[i]:
                i+=1
                j+=1
            elif s[j]!=t[i]:
                i+=1
        return j==len(s)





class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res=[]
        for i in range(len(s)-2):
            tres=""
            for j in range(i,i+3):
                tres+=s[j]
            res.append(tres)
        count=0
        for i in res:
            if len(set(i))==len(list(i)):
                count+=1
        return count

        

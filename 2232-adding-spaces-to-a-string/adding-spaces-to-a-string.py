class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(0)
        j=0
        res = ""
        for i in range(len(s)):
            if i!=spaces[j]:
                res+=s[i]
            elif i==spaces[j]:
                res+=" "
                res+=s[i]
                j+=1
        return res

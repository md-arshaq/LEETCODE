class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        # INEFFICIENT APPROACH 
        # spaces.append(0)
        # j=0
        # res = ""
        # for i in range(len(s)):
        #     if i!=spaces[j]:
        #         res+=s[i]
        #     elif i==spaces[j]:
        #         res+=" "
        #         res+=s[i]
        #         j+=1
        # return res

        res = []

        spaces.append(0)
        j=0
        count=0
        for i in s:
            if count!=spaces[j]:
                res.append(i)
                count+=1
            else:
                res.append(" ")
                res.append(i)
                j+=1
                count+=1
        return "".join(res)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i=0
        j=0
        l1 = len(word1)
        l2 = len(word2)
        while(i<l1 and j<l2):
            ans.append(word1[i])
            i+=1
            ans.append(word2[j])
            j+=1
        if l1>l2:
            ans.append(word1[i:])
        elif l1<l2:
            ans.append(word2[j:])

        return "".join(ans)
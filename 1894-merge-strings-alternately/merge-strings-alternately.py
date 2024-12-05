class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i=0
        j=0
        while(i<len(word1) and j<len(word2)):
            ans.append(word1[i])
            i+=1
            ans.append(word2[j])
            j+=1
        print(ans)
        if len(word1)>len(word2):
            ans.append(word1[i:])
        elif len(word1)<len(word2):
            ans.append(word2[j:])
        print(ans)

        return "".join(ans)
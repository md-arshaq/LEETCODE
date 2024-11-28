class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        i=0
        j=len(s)-1

        while(i<j):
            if lst[i] not in ['a', 'e', 'i', 'o','u','A', 'E', 'I', 'O', 'U']:
                i+=1
            if lst[j] not in ['a', 'e', 'i', 'o','u','A', 'E', 'I', 'O', 'U']:
                j-=1
            if ((lst[i] in ['a', 'e', 'i', 'o','u','A', 'E', 'I', 'O', 'U']) and (lst[j] in ['a', 'e', 'i', 'o','u','A', 'E', 'I', 'O', 'U'])):
                lst[i],lst[j]=lst[j],lst[i]
                j-=1
                i+=1

        return "".join(lst)

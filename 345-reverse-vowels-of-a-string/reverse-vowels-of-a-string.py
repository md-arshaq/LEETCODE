class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        i=0
        j=len(s)-1

        vowels = set('aeiouAEIOU')

        while(i<j):
            if lst[i] not in vowels:
                i+=1
            if lst[j] not in vowels:
                j-=1
            if ((lst[i] in vowels) and (lst[j] in vowels)):
                lst[i],lst[j]=lst[j],lst[i]
                j-=1
                i+=1

        return "".join(lst)

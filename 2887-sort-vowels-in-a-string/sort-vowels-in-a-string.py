class Solution:
    def sortVowels(self, s: str) -> str:
        l1 = list(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        l2 =[]
        for i in s:
            if i in vowels:
                l2.append(i)
        l2.sort()
        print(l2)
        j=0
        for i in range(len(l1)):
            if l1[i] in vowels:
                l1[i]=l2[j]
                j+=1

        return "".join(l1)
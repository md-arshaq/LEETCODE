class Solution:
    def sortVowels(self, s: str) -> str:

        # # APPROACH 1-EX BRUTE
        # l1 = list(s)
        # vowels = set("aeiouAEIOU")
        # vowel_list =[]
        # for ch in s:
        #     if ch in vowels:
        #         vowel_list.append(ch)
        # vowel_list.sort()
        # print(vowel_list)
        # j=0
        # for i in range(len(l1)):
        #     if l1[i] in vowels:
        #         l1[i]=l2[j]
        #         j+=1

        # return "".join(l1)

        # # APPROACH 2
        # vowels = set("aeiouAEIOU")
        # vowel_list =[]
        # for ch in s:
        #     if ch in vowels:
        #         vowel_list.append(ch)
        # vowel_list.sort()

        # res = []
        # j=0
        # for i in s:
        #     if i in vowels:
        #         res.append(vowel_list[j])
        #         j+=1
        #     else:
        #         res.append(i)
        # return "".join(res)

        #APPROACH 3

        vowels = set("aeiouAEIOU")
        vowel_list =[]
        for ch in s:
            if ch in vowels:
                vowel_list.append(ch)
        vowel_list.sort()

        s_list = list(s)
        j=0
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i]=vowel_list[j]
                j+=1
        return "".join(s_list)


       
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # FIRST APPROACH

        # cln = re.sub(r'[^a-zA-Z0-9]',"",s).lower()
        # i=0
        # j=len(cln)-1
        # while(i<j):
        #     if cln[i]==cln[j]:
        #         i+=1
        #         j-=1
        #     else:
        #         return False
        # return True

        # RECURSIVE APPROACH
        s = s.lower()
        i=0
        j=len(s)-1
        def palin(word,i,j):
            if i>=j:
                return True
            if not word[i].isalnum():
                return palin(word,i+1,j)
            if not word[j].isalnum():
                return palin(word,i,j-1)
            if word[i]==word[j]:
                return palin(word,i+1,j-1)
            else:
                return False

        return palin(s,i,j)
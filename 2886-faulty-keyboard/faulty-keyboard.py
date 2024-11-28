class Solution:
    def finalString(self, s: str) -> str:
        def rev(string):
            lst = list(string)
            i=0
            j=len(lst)-1
            while(i<j):
                lst[i],lst[j]=lst[j],lst[i]
                i+=1
                j-=1
            return "".join(lst)


        fin = ""
        for i in s:
            if i=="i":
                fin = rev(fin)
            else:
                fin+=i
        return fin
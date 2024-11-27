class Solution:
    def fib(self, n: int) -> int:
        #RECURSIVE APPROACH

        # def recursive(n):
        #     if n==0 or n==1:
        #         return n
        #     else:
        #         k = recursive(n-1)+recursive(n-2)
        #     return k
        
        # return recursive(n)

        if n==0 or n==1:
            return n
        a = 0
        b = 1
        for i in range(2,n+1):
            temp = a
            a = b
            b = temp+b
        return b






        
class Solution:
    def fib(self, n: int) -> int:
        def recursive(n):
            if n==0 or n==1:
                return n
            else:
                sum1 = recursive(n-1)+recursive(n-2)
            return sum1
        
        return recursive(n)



        
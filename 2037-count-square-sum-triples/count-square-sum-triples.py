class Solution:
    def countTriples(self, n: int) -> int:
        sqr = set()
        for i in range(n+1):
            sqr.add(i**2)
        
        count=0
        for i in range(1,n):
            for j in range(i+1,n):
                if i**2+j**2 in sqr:
                    count+=1
        
        return count*2
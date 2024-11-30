class Solution:
    def minPartitions(self, n: str) -> int:
        maxi = -1000
        for i in n:
            if int(i)>maxi:
                maxi = int(i)
        return maxi
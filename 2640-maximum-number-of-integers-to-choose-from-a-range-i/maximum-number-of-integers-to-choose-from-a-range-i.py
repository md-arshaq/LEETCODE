class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count=0
        sum1 = 0 
        banned_set =set(banned)
        for i in range(1,n+1):
            if i in banned_set:
                continue
            else:
                sum1+=i

            if sum1>maxSum:
                break
            else:
                count+=1
        return count

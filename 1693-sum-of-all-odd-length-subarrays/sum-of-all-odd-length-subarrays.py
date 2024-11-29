class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        finsum=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if len(arr[i:j+1])%2==1:
                    finsum = finsum+sum(arr[i:j+1])
        return finsum


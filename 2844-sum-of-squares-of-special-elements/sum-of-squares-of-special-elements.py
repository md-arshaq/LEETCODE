class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if len(nums)%(i+1)==0:
                res = res + nums[i]**2

        return res


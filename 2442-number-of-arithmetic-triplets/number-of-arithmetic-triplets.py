class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        #BRUTEST FORCEST

        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
        #                 count+=1
        # return count

        # USING HASH SET
        
        count=0
        hashset = set(nums)
        for i in nums:
            if (i+diff) in hashset and (i+2*diff) in hashset:
                count+=1
        return count


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> bool:
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        #BINARY SEARCH
        count = 0
        for i in nums:
            if self.binarySearch(nums,i+diff) and self.binarySearch(nums,i+2*diff):
                count+=1
        return count



        #BRUTEST FORCEST

        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
        #                 count+=1
        # return count

        # USING HASH SET
        
        # count=0
        # hashset = set(nums)
        # for i in nums:
        #     if (i+diff) in hashset and (i+2*diff) in hashset:
        #         count+=1
        # return count

        

        

        
             




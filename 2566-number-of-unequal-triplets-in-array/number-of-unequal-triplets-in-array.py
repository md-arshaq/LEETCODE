class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[i]!=nums[j]:
                    for k in range(j+1,len(nums)):
                        if nums[i] != nums[k] and nums[j] != nums[k]:
                            count+=1
        return count
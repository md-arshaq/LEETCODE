class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        print(nums)

        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        print(nums)

        while(j<len(nums)):
            nums[j]=0
            j+=1
        
        return nums
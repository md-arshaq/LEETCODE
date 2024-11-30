class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        # BRUTE FORCE 

        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] < target:
        #             count+=1
        # return count

        # TWO POINTERS

        nums.sort()
        low = 0
        high = len(nums)-1
        count=0
        while(low<high):
            if nums[low] + nums[high] < target:
                count+=(high-low)
                low+=1
            else:
                high-=1
        return count
        
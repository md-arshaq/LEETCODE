class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        bada=-1
        max_index=-1
        for i in range(len(nums)):
            if nums[i]>bada:
                bada=nums[i]
                max_index=i
        for i in range(len(nums)):
            if i!=max_index and bada<2*nums[i]:
                return -1
        return max_index
        
        
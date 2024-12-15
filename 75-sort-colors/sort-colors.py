class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count =Counter(nums)

        zero = count[0]
        ones = count[1]
        twos = count[2]

        idx = 0

        nums[idx:idx+zero]=[0]*zero
        idx =idx+zero
        nums[idx:idx+ones]=[1]*ones
        idx=idx+ones
        nums[idx:idx+twos]=[2]*twos

        
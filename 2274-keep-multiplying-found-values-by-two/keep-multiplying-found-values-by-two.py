class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        seen = set(nums)
        for i in nums:
            if original in seen:
                original*=2
        return original

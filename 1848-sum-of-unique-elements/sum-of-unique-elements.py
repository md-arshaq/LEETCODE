class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict1 = defaultdict(int)
        for i in nums:
            dict1[i]+=1

        sum1 = 0
        for key,val in dict1.items():
            if val==1:
                sum1+=key
        return sum1


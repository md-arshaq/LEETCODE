class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict1 = defaultdict(int)

        for i in nums:
            dict1[i]+=1

        print(dict1)

        maxi = max(dict1.values())

        print(maxi)

        ans = 0
        for i in dict1.values():
            if i==maxi:
                ans+=i
        
        return ans
                
        
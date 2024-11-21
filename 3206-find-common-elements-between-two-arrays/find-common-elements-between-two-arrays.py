class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dict1 = defaultdict(int)
        # dict2 = defaultdict(int)

        # for i in nums1:
        #     dict1[i]+=1

        # for i in nums2:
        #     dict2[i]+=1
        count1=0
        for i in nums1:
            if i in nums2:
                count1+=1
        count2=0
        for i in nums2:
            if i in nums1:
                count2+=1
                
        return [count1,count2]

        


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newlist=[]
        newlist = nums1+nums2
        newlist.sort()

        if len(newlist)%2==1:
            return newlist[len(newlist)//2]
        else:
            return (newlist[(len(newlist)//2)]+newlist[(len(newlist)//2)-1])/2
        
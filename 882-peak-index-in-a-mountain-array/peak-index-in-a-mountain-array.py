class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # LINEAR SOLUTION

        # max_index=0
        # for i in range(1,len(arr)):
        #     if (arr[i] > arr[max_index]):
        #         max_index = i
        # return max_index        

        # BINARY SEARCH SOLUTION

        low = 0
        high = len(arr)-1

        while(low<=high):
            mid = (low+high)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid+1]:
                high = mid-1
            elif arr[mid-1]<arr[mid+1]:
                low = mid+1
        


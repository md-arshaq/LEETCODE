# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, MountainArray: 'MountainArray') -> int:
        length = MountainArray.length()
        low = 1
        high = length-2
        while(low<=high):
            mid=(low+high)//2
            l = MountainArray.get(mid-1)
            m = MountainArray.get(mid)
            r = MountainArray.get(mid+1)
            if l<m<r:
                low=mid+1
            elif l>m>r:
                high=mid-1
            else:
                break
        peak=mid


        low = 0
        high = peak
        while(low<=high):
            mid = (low+high)//2
            val  = MountainArray.get(mid)
            if val>target:
                high = mid-1
            elif val<target:
                low = mid+1
            else:
                return mid


        low = peak
        high = length-1
        while(low<=high):
            mid = (low+high)//2
            val  = MountainArray.get(mid)
            if val>target:
                low = mid+1
            elif val<target:
                high = mid-1
            else:
                return mid

        return -1
        
        
            


                             

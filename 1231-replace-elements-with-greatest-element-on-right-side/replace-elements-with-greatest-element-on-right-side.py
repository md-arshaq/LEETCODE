class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        #THE BRUTE FROCE
        # tc = O(n2) -> TLE
        # for i in range(len(arr)-1):
        #     arr[i] = max(arr[i+1:])
        # arr[-1]=-1
        # return arr

        maxi= -1
        for i in range(len(arr)-1,-1,-1):
            val = arr[i]
            arr[i] = maxi
            maxi = max(maxi,val)
        return arr

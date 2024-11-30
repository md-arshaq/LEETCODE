class Solution:
    def binarySearch(self, nums: List[int], target: int) -> bool:
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

    def countTriples(self, n: int) -> int:
        l1 = []
        for i in range(1,n+1):
            l1.append(i)
        print(l1)
    
        sqr = set()
        for i in l1:
            sqr.add(i**2)
        print(sqr)
        
        count=0
        for i in range(len(l1)):
            for j in range(len(l1)):
                if i==j:
                    continue
                if l1[i]**2+l1[j]**2 in sqr:
                    count+=1
        
        return count
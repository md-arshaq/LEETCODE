class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        k =len(piles)-len(piles)//3
        piles.sort(reverse=True)
        sum1 = 0
        for i in range(1,k,2):
            sum1+=piles[i]
        return sum1

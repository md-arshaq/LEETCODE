class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        k =len(piles)-len(piles)//3
        print(k)
        piles.sort(reverse=True)
        print(piles)

        sum1 = 0
        for i in range(k+1):
            if i%2==1:
                sum1+=piles[i]
        return sum1

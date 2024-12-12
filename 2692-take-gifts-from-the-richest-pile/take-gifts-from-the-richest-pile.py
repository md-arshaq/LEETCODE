class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while(k!=0):
            maxi = max(gifts)
            for i in range(len(gifts)):
                if gifts[i]==maxi:
                    gifts[i]=int(sqrt(maxi))
                    break
            k-=1
        print(gifts)
        return sum(gifts)



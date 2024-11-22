class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        res = 0

        count1=1
        for i in s:
            dict1[i]=count1
            count1+=1
        print(dict1)

        count2=1
        for j in t:
            dict2[j]=count2
            count2+=1
        print(dict2)

        for i in s:
            res = res+ abs(dict1[i]-dict2[i])
        
        return res



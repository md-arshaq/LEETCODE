class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1 = defaultdict(int)

        for i in s:
            dict1[i]+=1

        x = list(dict1.values())[0]
        for i in dict1.values():
            if i!=x:
                return False
        return True

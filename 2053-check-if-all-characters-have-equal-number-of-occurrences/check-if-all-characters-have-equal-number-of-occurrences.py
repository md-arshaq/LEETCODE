class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1 = defaultdict(int)

        for i in s:
            dict1[i]+=1

        print(dict1)

        return len(set(dict1.values()))==1

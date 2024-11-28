class Solution:
    def countPoints(self, rings: str) -> int:
        dict1 = defaultdict(list)

        for i in range(1,len(rings)):
            if rings[i].isdigit():
                dict1[rings[i]].append(rings[i-1])
        print(dict1)
        
        count=0
        for i in dict1.values():
            if set(i)=={'B', 'G', 'R'}:
                count+=1
        return count

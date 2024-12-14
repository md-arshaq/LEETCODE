class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)

        count = Counter(students)
        print(count)

        for i in sandwiches:
            if count[i]>0:
                res-=1
                count[i]-=1
            else:
                return res
        return res
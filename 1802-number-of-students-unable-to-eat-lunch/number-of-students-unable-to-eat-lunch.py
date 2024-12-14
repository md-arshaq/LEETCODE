class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        # THE OPTIMAL ONE 
        # # res = len(students)

        # # count = Counter(students)
        # # print(count)

        # # for i in sandwiches:
        # #     if count[i]>0:
        # #         res-=1
        # #         count[i]-=1
        # #     else:
        # #         return res
        # # return res

        while(students):
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                x = students.pop(0)
                students.append(x)

            all_dislike = True

            for student in students:
                if student == sandwiches[0]:
                    all_dislike = False
                    break

            if all_dislike:
                break

        return len(sandwiches)


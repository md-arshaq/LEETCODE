class Solution:
    def removeStars(self, s: str) -> str:
        stack1=[]
        for i in s:
            if i=="*":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
        return "".join(stack1)
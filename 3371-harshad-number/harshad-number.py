class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum1 =0 
        for i in str(x):
            sum1+=int(i)
        if x%sum1==0:
            return sum1
        else:
            return -1

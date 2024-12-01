class Solution:
    def smallestNumber(self, n: int) -> int:
        i=n
        while(True):
            binary = bin(i)[2:]

            set_bit =True

            for j in binary:
                if j!='1':
                    set_bit = False
                    break
            
            if set_bit:
                return i

            i+=1

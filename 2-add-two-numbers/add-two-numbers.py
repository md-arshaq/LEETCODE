# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        temp1=l1
        i=1
        while(temp1!=None):
            num1 = num1+temp1.val*i
            i=i*10
            temp1=temp1.next
        print(num1)

        num2=0
        temp2=l2
        i=1
        while(temp2!=None):
            num2 = num2+temp2.val*i
            i=i*10
            temp2=temp2.next
        print(num2)

        fin = list(str(num1+num2))
        fin = fin[::-1]
        print(fin)

        dummy = ListNode(0)
        curr = dummy
        for i in fin:
            curr.next = ListNode(int(i))
            curr = curr.next

        return dummy.next

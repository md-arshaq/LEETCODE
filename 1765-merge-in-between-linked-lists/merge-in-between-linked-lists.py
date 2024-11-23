# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp2 = list2
        while(temp2.next!=None):
            temp2 = temp2.next
        

        count1=0
        front=list1
        while(count1!=a-1):
            front =front.next
            count1+=1

        count2=0
        back=list1
        while(count2!=b+1):
            back =back.next
            count2+=1

        front.next=list2
        temp2.next=back

        return list1


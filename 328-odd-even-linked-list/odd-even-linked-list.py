# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Dummy1 = ListNode()
        Dummy2 = ListNode()

        listOdd = Dummy1
        listEven = Dummy2

        count = 0
        temp = head
        while(temp!=None):
            if count%2==0:
                listOdd.next=temp
                listOdd = listOdd.next
            else:
                listEven.next=temp
                listEven = listEven.next
            temp = temp.next
            count+=1

        listEven.next = None
        listOdd.next = Dummy2.next

        return Dummy1.next
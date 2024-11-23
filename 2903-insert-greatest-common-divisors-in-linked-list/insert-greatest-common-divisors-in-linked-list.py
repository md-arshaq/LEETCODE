# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while(temp.next!=None):
            hcf = math.gcd(temp.val,temp.next.val)
            newnode = ListNode(val=hcf)
            
            newnode.next = temp.next
            temp.next = newnode

            temp = newnode.next
        return head

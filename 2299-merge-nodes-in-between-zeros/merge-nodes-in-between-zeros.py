# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy
        sum1 = 0
        temp=head.next
        while(temp!=None):
            if temp.val!=0:
                sum1+=temp.val
            elif temp.val==0:
                ans.next=ListNode(val=sum1)
                ans=ans.next
                sum1=0
            temp=temp.next
        return dummy.next


                



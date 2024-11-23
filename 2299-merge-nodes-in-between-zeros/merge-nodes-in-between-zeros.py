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

        # # Dummy node to hold the result list
        # current = ListNode() # Pointer to the current node in the result list
        # temp = head.next  # Skip the first zero node
        # sum1 = 0
        
        # while temp:
        #     if temp.val != 0:
        #         sum1 += temp.val
        #     else:  # Encountered a zero, segment ends
        #         current.next = ListNode(val=sum1)  # Add new node with the sum
        #         current = current.next  # Move to the new node
        #         sum1 = 0  # Reset the sum for the next segment
        #     temp = temp.next  # Move to the next node
        
        # return current.next  # Return the merged result list, skipping dummy

                



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        curr = head
        prev = None

        while curr is not None:
            next_node = curr.next # store next
            curr.next = prev # reverse current node's next
            prev = curr
            curr = next_node

        return prev
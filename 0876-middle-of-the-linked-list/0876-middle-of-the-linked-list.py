# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        return slow_pointer
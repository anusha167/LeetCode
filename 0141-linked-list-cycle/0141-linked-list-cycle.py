# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # if slow and fast pointers point to the same node again, a cycle must exist

        # initialize pointers
        slow = head
        fast = head
        
        while slow and fast and fast.next is not None:

            slow = slow.next # pointer moves one step
            fast = fast.next.next # pointer moves two steps

            if slow == fast: # if slow and fast point to same node
                return True
        return False

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            sum = digit1 + digit2 + carry
            tail.next = ListNode(sum % 10) #Isolate the last digit of the sum to store in the current node (e.g., 14 -> 4)
            carry = sum // 10 #Isolate the tens digit of the sum to carry over to the next loop (e.g., 14 -> 1)
            
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next
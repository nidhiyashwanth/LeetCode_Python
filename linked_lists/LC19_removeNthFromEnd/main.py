class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode("placeholder")
        dummy_head.next = head

        slow = dummy_head
        fast = dummy_head

        # Move fast n positions up
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy_head.next
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        dummy_head = ListNode("placeholder")
        dummy_head.next = head
        
        current = dummy_head
        while current:
            if current.next and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next

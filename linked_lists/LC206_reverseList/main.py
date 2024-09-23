# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            temp = current.next
            
            #change direction
            current.next = prev

            # Move prev and current up by 1 node
            prev = current
            current = temp
        return prev
    
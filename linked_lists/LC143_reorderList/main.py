class Solution:
    def reorderList(self, head):
        if not head:
            return
        
        slow = head
        fast = head
        # Find middle node and set it to slow
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split the LL to two LL with middle node . Reverse 2nd half
        second_head = self.reverseList(slow.next)
        slow.next = None

        # Zipper the two lists together
        current = head
        current2 = second_head
        while current2:
            current_next = current.next 
            current2_next = current2.next
            
            current.next = current2
            current2.next = current_next

            current = current_next
            current2 = current2_next
    
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
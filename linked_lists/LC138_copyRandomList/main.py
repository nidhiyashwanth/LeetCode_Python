class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        hash_table = {}
        current = head

        while current:
            hash_table[current] = Node(current.val, None, None)
            current = current.next
        
        current = head
        while current:
            if current.next:
                hash_table[current].next = hash_table[current.next]
            if current.random:
                hash_table[current].random = hash_table[current.random]
            current = current.next
        return hash_table[head]
    

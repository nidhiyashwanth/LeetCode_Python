from heapq import heappush, heappop
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        priority_queue = []
        dummy_head = ListNode("filler")
        
        for i in range(len(lists)):
            head_node = lists[i]
            if head_node:
                heappush(priority_queue, [head_node.val, i,  head_node])
        
        sorted_list_tail = dummy_head
        while priority_queue:
            dequeued = heappop(priority_queue)
            node = dequeued[2]
            sorted_list_tail.next = node

            if node.next:
                heappush(priority_queue, [node.next.val, dequeued[1], node.next])
            sorted_list_tail = sorted_list_tail.next
        return dummy_head.next
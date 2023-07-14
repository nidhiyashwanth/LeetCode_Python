from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums, k):
        priority_queue = []
        for num in nums:
            heappush(priority_queue, num)
            if len(priority_queue) > k:
                heappop(priority_queue)
        return priority_queue[0]
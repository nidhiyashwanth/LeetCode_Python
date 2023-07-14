from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums, k):
        dictionary = {}

        for n in nums:
            if n in dictionary:
                dictionary[n] += 1
            else:
                dictionary[n] = 1
        priority_queue = []

        for key in dictionary.keys():
            heappush(priority_queue, [dictionary[key], key])
            if len(priority_queue) > k:
                heappop(priority_queue)
        res = []
        while priority_queue:
            res.append(heappop(priority_queue)[1])
        return res
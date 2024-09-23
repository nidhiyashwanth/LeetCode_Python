from heapq import heappush, heappop
class Solution:
    def kClosest(self, points, K):
        max_heap = []
        for sub_array in points:
            x = sub_array[0]
            y = sub_array[1]

            distance = -(x * x + y * y)
            heappush(max_heap, [distance, sub_array])

            # Max heap will keep k smalltest distance
            if len(max_heap) > K:
                heappop(max_heap)

        res = []
        while max_heap:
            res.append(heappop(max_heap)[1])
        return res
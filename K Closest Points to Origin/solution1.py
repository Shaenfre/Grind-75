'''
Time complexity O(nlogk)
Space complexity O(k)
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x , y in points:
            heapq.heappush(heap, (-(x*x + y*y), x, y))
            while len(heap) > k:
                heapq.heappop(heap)

        return list((x,y) for _, x, y in heap)
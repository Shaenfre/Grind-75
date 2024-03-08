'''
Time complexity O(nlogn)
Space complexity O(n)

TODO: Do without sorting (larry reference)
'''
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        INF = 10 ** 20

        events = []
        for s, e, p in zip(startTime, endTime, profit):
            events.append([s, e, p])

        events.append([INF, INF, 0])
        events.sort()

        h = []
        best = 0

        for s, e, p in events:
            while len(h) > 0 and h[0][0] <= s:
                best = max(best, h[0][1])
                heapq.heappop(h)
            
            heapq.heappush(h, [e, best + p])

        return best
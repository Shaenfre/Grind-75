"""
Time complexity O(nlogn)
Space complexity O(n)
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        END = 0
        START = 1
        events = []

        for index, (s, e, p) in enumerate(zip(startTime, endTime, profit)):
            events.append((s, START, index))
            events.append((e, END, index))

        best_so_far = 0
        max_profits = [0] * N
        events.sort()

        for x, e, index in events:
            if e == START:
                max_profits[index] = profit[index] + best_so_far
            else:
                best_so_far = max(best_so_far, max_profits[index])

        return max(max_profits)


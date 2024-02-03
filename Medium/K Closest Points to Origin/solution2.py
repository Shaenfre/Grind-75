'''Time complexity O(nlogn)
Space complexity O(1)
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return list(sorted(points,key = lambda p: p[0] ** 2 + p[1] ** 2))[:k]
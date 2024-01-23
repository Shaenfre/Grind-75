# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

'''
Time complexity O(log(n))
Space complexity O(1)
When l = m + 1 or r = m - 1 in binary search do we need to do l < r and
not l <= r
'''

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l < r:
            m = (l + r) // 2
            # print(m)
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return r
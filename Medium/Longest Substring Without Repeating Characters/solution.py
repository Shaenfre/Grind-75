'''
Time complexity O(n)
Space complexity O(n)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        inset = set()
        best = 0

        for right in range(len(s)):
            while s[right] in inset:
                inset.remove(s[left])
                left += 1
            
            inset.add(s[right])
            best = max(best, right - left + 1)

        return best
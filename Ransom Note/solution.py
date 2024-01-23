'''
Time complexity O(m + n) m and n are length of strings
Space complexity O(l) number of unique letters
Implemented in python way
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)

        return all(r[k] <= m[k] for k in r.keys())
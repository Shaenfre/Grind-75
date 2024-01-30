'''
time complexity O(n)
space complexity O(1)

to do: implement in dp and divide and conquer way
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, ans = 0, -1000000
        for n in nums:
            sum += n
            ans = max(sum, ans)
            if sum < 0:
                sum = 0
        
        return ans
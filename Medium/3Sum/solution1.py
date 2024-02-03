'''
Time complexity O(n^2)
Space complexity O(n)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        N = len(nums)

        for i in range(N):
            count = collections.Counter(nums[i + 1 :])
            for j in range(i + 1, N):
                count[nums[j]] -= 1
                numk = -(nums[i] + nums[j])

                if numk >= nums[j] and count[numk] > 0:
                    s.add((nums[i], nums[j], numk))

        return list(s)

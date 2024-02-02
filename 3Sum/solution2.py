'''
Time complexity O(n**2)
Space compexity O(1)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        N = len(nums)

        print(nums)
        for i in range(N):
            sum = -nums[i]
            j, k = i + 1, N - 1
            print(sum)

            while j < k:
                # print(j, k)
                if nums[j] + nums[k] == sum:
                    s.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                    # print("hi")
                elif (nums[j] + nums[k]) < sum:
                    j += 1
                    # print("hello ", j)
                else:
                    k-=1
                    # print("wtf")

        return list(s)

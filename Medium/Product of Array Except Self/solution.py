'''
Time complexity O(n)
Space complexity O(1)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = list()
        product = 1
        size = len(nums)
        zero = False
        moreThanOneZero = False

        for num in nums:
            if num == 0:
                if zero:
                    moreThanOneZero = True

                zero = True
                continue

            product *= num

        if moreThanOneZero:
            return [0] * size

        for num in nums:
            if num == 0:
                ans.append(product)
            elif zero:
                ans.append(0)
            else:
                ans.append(product // num)

        return ans
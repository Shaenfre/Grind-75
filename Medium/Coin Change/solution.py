class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10 ** 20

        cache = [None] * (amount + 1)
        '''
        Time complexity: Number of inputs * Time taken per input
        Number of inputs: Amount (10**4)
        Time taken per input: Number of coins (12)
        12 * 10 **4

        Space complexity: Number of inputs * Space per input
        Space per input: 1
        10**4
        '''
        def getMin(amount):
            if cache[amount] is not None:
                return cache[amount]

            if amount == 0:
                return 0

            best = INF

            for c in coins:
                if amount - c >= 0:
                    best = min(best, 1 + getMin(amount - c))

            cache[amount] = best
            return best

        if getMin(amount) == INF:
            return -1
        
        return getMin(amount)

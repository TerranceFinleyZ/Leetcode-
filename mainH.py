class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = float('inf')
        max_profit = 0

        for i in prices:
            if i > x:
                max_profit += i-x
            x = i
        return max_profit
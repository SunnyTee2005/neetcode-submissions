class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,5,3,6,4]
        max_profit = 0
        min_p = prices[0]
        for p in range(len(prices)) :
            min_p = min(min_p, prices[p])
            max_profit = max(max_profit, prices[p] - min_p)
        return max_profit

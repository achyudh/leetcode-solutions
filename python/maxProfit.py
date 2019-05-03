class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        least = prices[0]
        max_profit = 0
        for i0 in prices:
            curr_profit = i0 - least
            if curr_profit > max_profit:
                max_profit = curr_profit 
            if i0 < least:
                least = i0
        return max_profit

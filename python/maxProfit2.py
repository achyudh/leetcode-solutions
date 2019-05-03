class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        i0 = 0
        profit = 0
        while i0 < len(prices) - 1:
            while i0 < len(prices) - 1 and prices[i0] >= prices[i0+1]:
                i0 += 1
            floor = prices[i0]
            while i0 < len(prices) - 1 and prices[i0] <= prices[i0+1]:
                i0 += 1
            ceiling = prices[i0]
            profit += (ceiling - floor)
        return profit

# Alternate Solution
class AltSolution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        i0 = 0
        profit = 0
        while i0 < len(prices) - 1:
            if prices[i0] < prices[i0+1]:
                profit += (prices[i0+1] - prices[i0])                
            i0 += 1
        return profit
            

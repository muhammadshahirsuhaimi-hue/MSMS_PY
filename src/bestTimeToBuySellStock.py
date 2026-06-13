class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if (prices[left] < prices[right]):
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            right += 1
        return maxProfit
            
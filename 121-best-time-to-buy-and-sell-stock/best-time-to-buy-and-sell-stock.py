class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_pnl = 0
        min_price = float("inf")
        for i in prices:
            pnl = i - min_price
            max_pnl = max(pnl, max_pnl)
            min_price = min(i, min_price)
        return max_pnl
        
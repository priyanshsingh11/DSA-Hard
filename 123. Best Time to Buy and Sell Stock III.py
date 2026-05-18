class Solution(object):
    def maxProfit(self, prices):
        firstbuy = float('-inf')
        firstsell = 0

        secondbuy = float('-inf')
        secondsell = 0

        for price in prices:
            firstbuy = max(firstbuy, -price)
            firstsell = max(firstsell, firstbuy + price)
            secondbuy = max(secondbuy, firstsell - price)
            secondsell = max(secondsell, secondbuy + price)

        return secondsell

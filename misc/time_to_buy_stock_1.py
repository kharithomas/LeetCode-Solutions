# finds the best time to purchase stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = 9999999
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]

            if prices[i] - minBuy > maxProfit:
                maxProfit = prices[i] - minBuy

        return maxProfit


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minValue = prices[0]
        thisTurn = prices[0]
        for i in range(len(prices)):
            if minValue > prices[i]:
                minValue = prices[i]
            thisTurn = prices[i] - minValue
            if profit < thisTurn:
                profit = thisTurn
        return profit
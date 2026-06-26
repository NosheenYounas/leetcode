class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        l , r = 0, 1
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices [l]
                res += profit
            l=r
            
        return res
        
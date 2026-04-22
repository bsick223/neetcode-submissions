class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Input: prices = [10,1,5,6,7,1]

        # Output: 6

        l = 0
        maxP = 0


        for r in range(1, len(prices)):
            

            if (prices[r] > prices[l]):
                profit = prices[r] - prices[l]
                if profit > maxP:
                    maxP = profit
            
            else:
                l = r
            

        return maxP

            
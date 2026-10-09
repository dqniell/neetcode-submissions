class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices): 
            if prices[left] < prices[right]: 
                difference = prices[right] - prices[left]
                maxProfit = max(difference, maxProfit)
            else: 
                left = right
            right+=1
        
        return maxProfit
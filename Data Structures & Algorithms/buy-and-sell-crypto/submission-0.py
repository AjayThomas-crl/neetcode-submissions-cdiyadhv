class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        n=len(prices)
        r=n-1

        profit=0
        
        while l<r:
            if prices[r]-prices[l]>0:
                profit=max(prices[r]-prices[l],profit)
            l+=1
            r-=1
        return profit
            
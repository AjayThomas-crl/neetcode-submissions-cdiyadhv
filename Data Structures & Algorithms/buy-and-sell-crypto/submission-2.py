class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        n=len(prices)
        r=n-1

        
        mr=0
        ml=sys.maxsize
        while l<r or l==r:
            mr=max(mr,prices[r])
            ml=min(ml,prices[l])
            r-=1
            l+=1
        print(mr,ml)
        return 0 if mr-ml<0 else mr-ml
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        n=len(prices)
        
        p=0
        mil=sys.maxsize
        for i in range (1,n):
            mil=min(mil,prices[i-1])
            if prices[i]-mil>0:
                p=max(p,prices[i]-mil)
        return p
        # ml=sys.maxsize
        # while l<r or l==r:
        #     mr=max(mr,prices[r])
        #     ml=min(ml,prices[l])
        #     r-=1
        #     l+=1
        # print(mr,ml)
        # return 0 if mr-ml<0 else mr-ml
            
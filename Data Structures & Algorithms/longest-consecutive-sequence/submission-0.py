class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max=1
        
        d=set()
        for i in nums:
            d.add(i)
        i=0
        mini=min(d)
        while len(d)>0:
            mini=min(d)
            d.remove(mini)
            if len(d)==0:
                return max
            if mini+1==min(d):
                max+=1
            else:
                return max
        return max


        

                
        
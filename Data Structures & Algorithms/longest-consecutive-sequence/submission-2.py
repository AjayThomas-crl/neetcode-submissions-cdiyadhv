class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum=1
        if not nums:
            return 0
        d=set()
        for i in nums:
            d.add(i)
        i=0
        mini=min(d)
        tempmax=1
        while len(d)>0:
            mini=min(d)
            print(mini)
            d.remove(mini)
            
            if len(d)==0:
                return maximum
            if mini+1==min(d):
                tempmax+=1
            else: 
                tempmax=1
            maximum=max(tempmax,maximum)
        return maximum


        

                
        
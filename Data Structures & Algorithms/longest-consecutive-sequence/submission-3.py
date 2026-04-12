class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum=0
        
        d=set(nums)
       
        i=0

        for i in d:
            if i-1 not in d:
                l=1
                while i+l in d:
                    l+=1
                maximum=max(l,maximum)
        return maximum
        


        

                
        
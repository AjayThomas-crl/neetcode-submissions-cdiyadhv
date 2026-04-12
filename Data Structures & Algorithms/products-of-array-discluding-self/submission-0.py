class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]*len(nums)
        suff=[1]*len(nums)
        res=[1]*len(nums)
        p=1

        for i in range (1,len(nums),1):
            p=p*nums[i-1]
            pref[i]=p
        
        s=1
        for i in range (len(nums)-1,-1,-1):
            
            
            suff[i]=s
            s=s*nums[i]
        
        for i in range (len(nums)):
            res[i]=pref[i]*suff[i]
            
        print(res)
        return res

        
        
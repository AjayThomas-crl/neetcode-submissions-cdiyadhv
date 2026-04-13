class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted(nums)
        l=0
        r=len(nums)-1
        m=int(len(nums)/2)

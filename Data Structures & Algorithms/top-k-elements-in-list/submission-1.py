class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        bucket=[0]*(len(nums)+1)
        res=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        print(d)
        for key,value in d.items():
            print(value)
            bucket[value]=key
        print(bucket)
        t=0
        for i in range(len(nums),0,-1):
            if bucket[i]>0:
                res.append(bucket[i])
                t+=1
            if t==k:
                break
        return res       
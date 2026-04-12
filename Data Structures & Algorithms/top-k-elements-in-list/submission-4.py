class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        bucket=[[] for _ in range(len(nums)+1)]
        res=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        print(d)
        for key,value in d.items():
            print(value)
            bucket[value].append(key)
        print(bucket)
        t=0
        for i in range(len(nums),0,-1):
            if bucket[i]!=0:
                res.extend(bucket[i])
                t+=1
            if len(res)==k:
                break
        return res       
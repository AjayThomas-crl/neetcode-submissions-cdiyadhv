class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        res=[]
        
        
        for i in range (len(strs)):
            st=strs[i]
            alpha=[0]*26
            for j in range (len(st)):
                alpha[ord(st[j])-97]+=1
            tup=tuple(alpha)
            if tup in d:
                d.get(tup).append(st)
            else:
                d[tup]=[st]
        
        for key, value in d.items():
            res.append(value)
            
        
        return res

            
               

                


        
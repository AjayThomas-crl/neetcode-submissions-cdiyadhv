class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        if(not strs):
            return ""
        for i in strs:
            res+=f"{len(i)}#{i}"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        if not s:
            return []
        
        st=""
        i=0
        while i<len(s):
            if s[i].isdigit():
                j=i
                while s[i].isdigit():
                    i+=1
                num=int(s[j:i])
            if s[i]=="#":
                st=s[i+1:i+num+1]
                res.append(st)
                i=i+num+1

        print(res)
        return res

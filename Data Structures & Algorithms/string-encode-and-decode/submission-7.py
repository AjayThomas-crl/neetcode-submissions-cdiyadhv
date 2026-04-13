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
        for i in range (len(s)):
            if s[i]=='#':
                st=s[i+1:i+int(s[i-1])+1]
                res.append(st)
                i=i+int(s[i-1])+1
        print(res)
        return res

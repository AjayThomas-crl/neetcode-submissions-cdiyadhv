class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        if(not strs):
            return ""
        for i in strs:
            res+=f"{i}~"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        if not s:
            return []
        res=s.strip("~").split("~")
        print(res)
        return res

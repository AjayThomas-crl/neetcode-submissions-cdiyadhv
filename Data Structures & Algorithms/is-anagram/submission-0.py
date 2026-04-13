class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in range (len(s)):
            d[s[i]]=d.get(s[i],0)+1
        
        for i in range (len(t)):
            if(d[t[i]]>1):
                d[t[i]]=d[t[i]]-1
            elif (d[t[i]]==0):
                d.pop(t[i])
        
        if(d):
            return False
        else:
            return True
        
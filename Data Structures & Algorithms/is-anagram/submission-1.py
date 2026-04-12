class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in range (len(s)):
            d[s[i]]=d.get(s[i],0)+1
        print(d)
        for i in range (len(t)):
            if t[i] not in d:
                return False
            elif  d[t[i]]>1:
                d[t[i]]=d[t[i]]-1
            else:
                d.pop(t[i])
        
        if d:
            return False
        else:
            return True
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s)-1
        regex = re.compile('[a-zA-Z0-9]')
        while l!=r and l<len(s) and r>-1 :
            print(bool(regex.search(s[l])))
            if not bool(regex.search(s[l])):
                l+=1
                continue
            if not bool(regex.search(s[r])):
                r-=1
                continue
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        
        return True
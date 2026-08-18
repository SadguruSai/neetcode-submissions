class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        def check_pali(left,right):
            nonlocal ans
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left-=1
                right+=1
                ans+=1
        
        for i in range(len(s)):
            left,right=i,i
            check_pali(left,right)
            left,right=i,i+1
            check_pali(left,right)            
        return ans
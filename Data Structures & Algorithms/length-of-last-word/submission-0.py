class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        left=0
        right=0
        for i in range(len(s)):
            if(s[i].isalpha() and s[i-1].isalpha()):
                right+=1
            if(s[i].isalpha() and s[i-1]==' '):
                left=i
                right=i+1
        return right-left

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq=set()
        ans=0
        max_l=0
        left=0
        for i in range(len(s)):
            while s[i] in freq:
                freq.remove(s[left])
                left+=1
            freq.add(s[i])
            l=i-left+1
            max_l=max(l,max_l)
        return max_l
            
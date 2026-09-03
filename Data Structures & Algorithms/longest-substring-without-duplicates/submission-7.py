class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq=set()
        l=0
        max_len=0
        for r in range(len(s)):
            while s[r] in freq:
                freq.remove(s[l])
                l+=1
            freq.add(s[r])
            max_len=max(r-l+1,max_len)
        return max_len
            
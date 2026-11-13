class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        l=0
        max_fre=0
        max_len=0
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]]=0
            freq[s[i]]+=1
            
            max_fre=max(freq[s[i]],max_fre)

            while((i-l+1)- max_fre > k):
                freq[s[l]]-=1
                l+=1
            
            max_len=max(i-l+1,max_len)
        return max_len

            
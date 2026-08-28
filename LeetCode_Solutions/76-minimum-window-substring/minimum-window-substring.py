class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        if m>n:
            return ""
        satisfied=0
        hash1=defaultdict(int)
        for i in t:
            hash1[i]+=1
        need=len(hash1)
        hash2=defaultdict(int)
        left,right=0,0
        ans=(-1,-1)
        min_len=float('inf')
        for right in range(n):
            hash2[s[right]]+=1
            if hash2[s[right]]==hash1[s[right]]:
                satisfied+=1
            while(satisfied==need):
                if right-left+1<min_len:
                    min_len=right-left+1
                    ans=(left,right)
                hash2[s[left]]-=1
                if hash2[s[left]]<hash1[s[left]]:
                    satisfied-=1
                left+=1
        l,r=ans
        return s[l:r+1]
            

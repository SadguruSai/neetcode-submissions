class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sett=defaultdict(int)
        for i in s:
            sett[i]+=1
        for i in t:
            sett[i]-=1
            if sett[i]<0:
                return False
        return True
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        ans=r
        def canShip(cap):
            ships,currCap=1,cap
            for w in weights:
                if(currCap-w<0):
                    currCap=cap
                    ships+=1
                currCap-=w
            return ships<=days
                
        while(l<=r):
            m=l+(r-l)//2
            if(canShip(m)):
                ans=min(ans,m)
                r=m-1
            else:
                l=m+1
        return ans


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        par=[i for i in range(n)]
        rank=[1]*n
        res=n
        def find(n1):
            node=n1
            while node!=par[node]:
                par[node]=par[par[node]]
                node=par[node]
            return node
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                par[p2]=p1
            else:
                rank[p2]+=rank[p1]
                par[p1]=p2
            return 1
        
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    res-=union(i,j)
        return res


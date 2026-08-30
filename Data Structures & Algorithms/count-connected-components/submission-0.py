class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        compo=0

        visited=set()

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
    
        for i in range(n):
            if i not in visited:
                compo+=1
                dfs(i)

        return compo
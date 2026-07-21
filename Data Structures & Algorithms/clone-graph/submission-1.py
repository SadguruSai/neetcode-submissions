"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self,oldtoNew,node):
        if not node:
            return None
        if node in oldtoNew:
            return oldtoNew[node]
        else:
            copy = Node(node.val)
            oldtoNew[node]=copy
            for node in node.neighbors:
                copy.neighbors.append(self.dfs(oldtoNew,node))
        return copy

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not Node:
            return None
        oldtoNew={}  
        return self.dfs(oldtoNew,node)
    
        


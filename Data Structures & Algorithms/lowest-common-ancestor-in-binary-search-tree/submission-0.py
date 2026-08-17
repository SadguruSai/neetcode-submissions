# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        new=root
        while new:
            if(p.val<new.val and q.val<new.val):
                new=new.left
            elif(p.val>new.val and q.val>new.val):
                new=new.right
            else:
                return new
        return q

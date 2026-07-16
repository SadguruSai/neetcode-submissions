# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def SameTree(self,p,q):
        if(p==None and q==None):
            return True
        elif(p and q and p.val==q.val):
            return self.SameTree(p.left,q.left) and self.SameTree(p.right,q.right)
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(subRoot==None):
            return True
        if(root==None):
            return False
        if(self.SameTree(root,subRoot)):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create a list to stor the ans
        #write the reccursive inorder traveral function
        #finish by returning ans
        ans=[]
        if root==None:
            return []
        ans.append(root.val)
        ans=ans+self.preorderTraversal(root.left)
        ans=ans+self.preorderTraversal(root.right)
        return ans
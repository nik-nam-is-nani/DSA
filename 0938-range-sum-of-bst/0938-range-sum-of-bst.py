# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,ans,low,high):
        if not root :
            return
        if low<=root.val<=high:
            ans[0]+=root.val
        if root.left:
            # ans+=root.val

            self.DFS(root.left,ans,low,high)
        if root.right:
            # ans+=root.val
            self.DFS(root.right,ans,low,high)
        if not root.left and not root.right:
            return 
        
            
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=[]
        ans.append(0)
        self.DFS(root,ans,low,high)
        return ans[0]
        
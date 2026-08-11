# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,ans,pre,now):
        # if not root:
        #     return 
        if root.left:
            self.DFS(root.left,ans,now,now-1)
        # if root.left and root.right:
        #     self.DFS(root.left)
        if root.right:
            self.DFS(root.right,ans,now,now+1)
        if not root.left and not root.right and now <pre:
            ans[0]+=root.val

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        if not root.left and not root.right:
            return 0
        dic=[0]
        i=0
        self.DFS(root,ans,0,0)
        return ans[0]
        
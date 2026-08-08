# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,height,ans):
        if root.right:
            self.DFS(root.right,height+1,ans)
        if root.left:
            self.DFS(root.left,height+1,ans)
        if not root.left and not root.right:
            ans[0] = min(ans[0],height+1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = [float("inf")]
        he=0
        self.DFS(root,he,ans)
        return ans[0]
        
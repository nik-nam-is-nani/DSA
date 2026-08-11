# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,ans):
        if not root:
            return 
        if root.left:
            self.DFS(root.left,ans)
        if root.right:
            self.DFS(root.right,ans)
        if not root.left and not root.right:
            ans.append(root.val)
            return
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans1=[]
        ans2=[]
        self.DFS(root1,ans1)
        self.DFS(root2,ans2)
        return ans1==ans2
        
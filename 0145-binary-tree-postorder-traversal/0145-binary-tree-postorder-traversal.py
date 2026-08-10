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
        ans.append(root.val)
        if not root.left and not root.right:
            return

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.DFS(root,ans)
        return ans

        
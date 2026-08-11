# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,value,flag):
        if not root:
            return
        if root.val!=value:
            flag[0]=False
            return 
            
        if root.left:
            self.DFS(root.left,value,flag)
        if root.right:
            self.DFS(root.right,value,flag)
        if not root.left and not root.right:
            return

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value=root.val

        flag=[True]
        self.DFS(root,value,flag)
        return flag[0]


        
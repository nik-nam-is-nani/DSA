# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,node,che):
        if not node:
            return 0
        right=self.DFS(node.right,che)
        left=self.DFS(node.left,che)
        bal=abs((right-left))
        if bal>1:
            che[0]=False

        return max(left,right)+1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check=[True]
        if not root:
            return check[0]
        self.DFS(root,check)
        return check[0]
        
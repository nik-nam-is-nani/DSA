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
        ans.append(root.val)
        if root.left:
            self.DFS(root.left,ans)
        if root.right:
            self.DFS(root.right,ans)
        if not root.left and not root.right:
            return

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        ans = []
        self.DFS(root, ans)
        
        seen = set()
        for val in ans:
            complement = k - val
            if complement in seen:
                return True
            seen.add(val)
            
        return False
        
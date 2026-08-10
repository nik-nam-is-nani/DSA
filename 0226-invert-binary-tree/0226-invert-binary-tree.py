# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root):
        if not root:
            return
        # if root.left and root.right:
        root.left,root.right=root.right,root.left
    
        self.DFS(root.left)
        self.DFS(root.right)
        # if not root.left and nnot root.right:
        #     return 

        
        # if root.left:
        #     a=root.val
        #     self.DFS(root.left)
        # if root.right:
        #     b=root.val
        #     self.DFS(root.left)
        # ans.append(b)
        # ans.append(a)
        if not root.left and not root.right:
            return root
        
        


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root1=root
        
        self.DFS(root)
        return root1

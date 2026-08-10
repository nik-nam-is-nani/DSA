# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     va=[]
#     def DFS(self,root,ans,va):
#         if not root :
#             return 
#         if root.left:
#             ans.append(root.val)
#             self.DFS(root.left,ans,va)
#         if root.right:
#             ans.append(root.val)
#             self.DFS(root.right,ans,va)
#         if not root.left and not root.right:
#             ans.append(root.val)
#             va.append(f"{ans[i-1]}->{ans[i]}" for i in range(1,len(and)))
#             ans=[]
#             return 
    
                



#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                result.append(path)
                return

            if node.left:
                dfs(node.left, path + "->")
            if node.right:
                dfs(node.right, path + "->")

        dfs(root, "")
        return result
        
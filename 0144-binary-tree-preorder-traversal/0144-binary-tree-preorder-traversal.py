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
            # ans.append(root.val)
            self.DFS(root.left,ans)
        # ans.append(root.val)
        if root.right:
            # ans.append(root.val)
            self.DFS(root.right,ans)

        if not root.left and  not root.right:
            # ans.append(root.val)
            return       

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if not root:
            return ans
        self.DFS(root,ans)
        return ans

        
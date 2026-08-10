# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # va=0
    # def BFS(self,root,va,bol):
    #     print(va)

    #     if root.right:

    #         return self.BFS(root.right,va+root.val,bol)
    #     if root.left:
    #         return self.BFS(root.left,va+root.val,bol)
    def DFS(self, root, va,targetSum):
        current_sum = va + root.val
        # if not root:
        #     if current_sum!=targetSum:
        #         return False
        if not root.left and not root.right:
            return current_sum==targetSum
        right_res=False
        left_res=False


        
        # if current_sum==targetSum:
        #     return True

        if root.right:
            right_res=self.DFS(root.right, current_sum,targetSum)
        if root.left:
            left_res=self.DFS(root.left, current_sum,targetSum)
        return right_res or left_res

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        va=0
        # bol=False
        a=self.DFS(root,va,targetSum)
        if a:
            return True
        else:
            return False

        

        
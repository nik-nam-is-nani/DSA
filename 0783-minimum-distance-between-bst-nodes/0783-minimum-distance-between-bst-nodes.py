# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        ans=[]
        nums=[]
        ans.append(root)
        while ans:
            node=ans.pop(0)
            nums.append(node.val)
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            
        nums.sort()
        mi=float('inf')
        for i in range(len(nums)-1):
            mi=min(mi,nums[i+1]-nums[i])
        return mi



        
        
        
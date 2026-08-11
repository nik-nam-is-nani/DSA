# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        ans=[]
        nums=[]
        nums.append(root)
        temp=[]
        che=1
        while nums:
            node=nums.pop(0)
            temp.append(node.val)
            if node.left and node.right:
                if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                    return False
            if node.left:
                nums.append(node.left)
            if node.right:
                nums.append(node.right)
            che-=1
            if che==0:
                if x in temp  and y in temp:
                    return True
                temp=[]
                che=len(nums)
        return False
            
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        temp=[]
        check=1
        nums=[]
        nums.append(root)
        while nums:
            node=nums.pop(0)
            temp.append(node.val)
            if node.left:
                nums.append(node.left)
            if node.right:
                nums.append(node.right)
            check-=1
            if check==0:
                ans.append(temp)
                temp=[]
                check=len(nums)
        ans.reverse()
        return ans
        
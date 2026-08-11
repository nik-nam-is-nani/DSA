# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nums = deque()
        nums.append(root)
        ans = []
        temp = []
        check = 1
        while nums:
            node = nums.popleft()
            check-=1
            temp.append(node.val)
            if node.left:
                nums.append(node.left)
            if node.right:
                nums.append(node.right)
            if check==0:
                ans.append(temp)
                temp=[]
                check = len(nums)
        return ans
            
        
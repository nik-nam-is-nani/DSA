# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        nums=[]
        temp=[]
        flag=False
        check = 1
        nums.append(root)
        while nums:
            node = nums.pop(0)
            check-=1
            temp.append(node.val)
            if node.left:
                nums.append(node.left)
            if node.right:
                nums.append(node.right)
            if check == 0:
                if not flag:
                 flag=True
                 ans.append(temp)
                 temp=[]
                else:
                    temp.reverse()
                    ans.append(temp)
                    temp=[]
                    flag=False
                check  = len(nums)
        return ans
        

        
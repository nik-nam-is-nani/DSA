# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    con=0
    def __init__(self):
        self.ans=0
    def BFS(self,root):
        if not root:
            return 0,0 
        # if root.left:
        left_sum,left_count=self.BFS(root.left)
        # if root.right:
        right_sum,right_count=self.BFS(root.right)
        total_sum=left_sum+right_sum+root.val
        total_count=left_count+right_count+1
        if root.val==(total_sum//total_count):
            self.ans+=1
        return total_sum,total_count

        # if (root.val+s1,s2)//(con+c1+c2)==root.val:
        #     ans[0]+=1
        # return root.val+s1+s2,con+c1,c2

        # if  not root.right and not root.left:
        #     return 0,0



    def averageOfSubtree(self, root: TreeNode) -> int:
        self.BFS(root)
        return self.ans
        
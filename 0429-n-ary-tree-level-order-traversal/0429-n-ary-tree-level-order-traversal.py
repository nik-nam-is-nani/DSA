"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        nums=deque()
        ans=[]
        temp = []
        nums.append(root)
        check = 1
        while nums:
            node=nums.popleft()
            temp.append(node.val)
            check-=1
            for child in node.children:
                nums.append(child)
            if check==0:
                ans.append(temp)
                temp=[]
                check = len(nums)
        return ans
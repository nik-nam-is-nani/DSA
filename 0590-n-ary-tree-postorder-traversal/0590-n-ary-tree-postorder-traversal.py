"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def dfs(self,node,ans):
        if not node: 
            return []
        for child in node.children:
            self.dfs(child,ans)
        ans.append(node.val)
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.dfs(root,ans)
        return ans
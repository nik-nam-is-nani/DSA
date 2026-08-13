"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        def DFS(root,ans):


            if not root:
                return 
            if root.children:
                ans.append(root.val)
                for child in root.children:
                    DFS(child,ans)
            if not root.children:
                ans.append(root.val)
                return ans
        DFS(root,ans)
        return ans

        # if not root:
        #     return 
        # nums=deque()
        # ans=[]
        # nums.append(root)
        # while nums:
        #     node=nums.pop()
        #     ans.append(node.val)
        #     for ch in node.children:
        #         nums.append(ch)
        # return ans

            
            
    


        
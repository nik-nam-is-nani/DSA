from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = deque(s)
        
        for char in t:
            if not ans:
                break
            if char == ans[0]:
                ans.popleft()
                
        return len(ans) == 0
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def DFS(s,open,close):
            
            if len(s)==2*n:
                ans.append(s)
                return 
            if open<n:
                DFS(s+"(",open+1,close)
            if close<open:
                DFS(s+")",open,close+1)
        DFS("",0,0)
        return ans
        
        
        
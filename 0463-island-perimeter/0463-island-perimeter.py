class Solution:
    def BFS(self,grid,visited,i,j):
        if i<0 or i==len(grid) or j<0 or j==len(grid[0]):
            return 1
        if visited[i][j]==1:
            return 0
        if grid[i][j] == 0:
            return 1
        visited[i][j]=1
        dic=[(-1,0),(1,0),(0,-1),(0,1)]
        ans = 0
        for ir,jc in dic:
            ir+=i
            jc+=j
            ans+=self.BFS(grid,visited,ir,jc)
        return ans




    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=[]
        for i in range(len(grid)):
            visited.append([0]*len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    # visited[i][j]=1
                     return self.BFS(grid,visited,i,j)
        return 0
        # cn=0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         count = 0
        #         if grid[i][j] == 1:
        #             if i==0 or grid[i-1][j]==0:
        #                 count+=1
        #             if i==len(grid)-1 or grid[i+1][j]==0:
        #                 count+=1
        #             if j==len(grid[0])-1 or grid[i][j+1]==0:
        #                 count+=1
        #             if j == 0 or grid[i][j-1]==0:
        #                 count+=1
        #             cn+=count
        # return cn

        
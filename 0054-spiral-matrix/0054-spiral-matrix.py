class Solution:
#     def DFS(self,matrix,i,j,ans,visited):
#         if 0<=j<len(matrix[0]) and 0<=i<len(matrix):
        
#             if 0<=j<len(matrix[0]) and 0<=i<len(matrix) and not visited[i][j]:
#                 ans.append(matrix[i][j])
#                 visited[i][j]=1
#                 self.DFS(matrix,i,j+1,ans,visited)
#             i+=1
#             if 0<=i<len(matrix) and 0<=j<len(matrix[0]) and not  visited[i][j]:
#                 ans.append(matrix[i][j])
#                 visited[i][j]=1
#                 self.DFS(matrix,i+1,j,ans,visited)
#             # i-=1
#             j-=1
#             if 0<=j<len(matrix[0]) and 0<=i<len(matrix) and not visited[i][j]:
#                 ans.append(matrix[i][j])
#                 visited[i][j]
#                 self.DFS(matrix,i,j-1,ans,visited)
#             i-=1
            
#             # j+=1

#             if 0<=i<len(matrix[0]) and 0<=j<len(matrix[0]) and not  visited[i][j]:
#                 ans.append(matrix[i][j])
#                 visited[i][j]=1
#                 self.DFS(matrix,i-1,j,ans,visited)
#             i+=1
#             j+=1
#         else:
#             return 

        
        
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top=0
        bottom=len(matrix)-1
        left=0
        ans=[]
        right=len(matrix[0])-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
            bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
            left+=1
        return ans

#         ans=[]
#         visited=[]
#         for i in range(len(matrix)):
#             visited.append([0]*len(matrix[0]))
#         self.DFS(matrix,0,0,ans,visited)
#         return ans
        
# from typing import List

# class Solution:
#     def DFS(self, matrix, i, j, ans, visited):
#         # Base check: ensure current bounds and not already visited
#         if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])) or visited[i][j]:
#             return

#         # Visit current cell
#         ans.append(matrix[i][j])
#         visited[i][j] = 1

#         # 1. Try moving RIGHT as far as possible
#         while j + 1 < len(matrix[0]) and not visited[i][j + 1]:
#             self.DFS(matrix, i, j + 1, ans, visited)

#         # 2. Try moving DOWN as far as possible
#         while i + 1 < len(matrix) and not visited[i + 1][j]:
#             self.DFS(matrix, i + 1, j, ans, visited)

#         # 3. Try moving LEFT as far as possible
#         while j - 1 >= 0 and not visited[i][j - 1]:
#             self.DFS(matrix, i, j - 1, ans, visited)

#         # 4. Try moving UP as far as possible
#         while i - 1 >= 0 and not visited[i - 1][j]:
#             self.DFS(matrix, i - 1, j, ans, visited)

#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return []

#         ans = []
#         visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]

#         # Start DFS at (0, 0)
#         self.DFS(matrix, 0, 0, ans, visited)
#         return ans
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col=[0]*len(matrix)
        row=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row[j]=1
                    col[i]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[j] or col[i]:
                    matrix[i][j]=0
        

        """
        Do not return anything, modify matrix in-place instead.
        """
        
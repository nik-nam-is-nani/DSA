class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited=[]
        nums=[]
        nums.append((sr,sc))
        value=image[sr][sc]
        visited.append((sr,sc))
        image[sr][sc]=color
        while nums:
            i,j=nums.pop(0)
            for ro,cl in [(0,-1),(0,1),(1,0),(-1,0)]:
                if (ro+i,cl+j) not in visited and  0<=ro+i<len(image) and 0<=cl+j<len(image[0]) and image[ro+i][cl+j]==value:
                    nums.append((ro+i,cl+j))
                    image[ro+i][cl+j]=color
                    visited.append((ro+i,cl+j))
        return image
                


            



        
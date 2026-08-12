class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[1]
        if numRows==1:
            return [ans]
        
        total=[]
        total.append(ans)
        total.append([1,1])
        i=0
        ans=[]
        while numRows-1>1:
            ans.append(1)
            for i in range(0,len(total[-1])):
                ans.append(sum(total[-1][i:i+2]))
            # ans.append(1)
            total.append(ans)
            ans=[]
            numRows-=1
        return total
        



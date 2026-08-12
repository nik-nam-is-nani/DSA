class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[1]
        if rowIndex==0:
            return ans
        
        total=[]
        total.append(ans)
        total.append([1,1])
        i=0
        ans=[]
        while rowIndex>1:
            ans.append(1)
            for i in range(0,len(total[-1])):
                ans.append(sum(total[-1][i:i+2]))
            # ans.append(1)
            total.append(ans)
            ans=[]
            rowIndex-=1
        return total[-1]
        
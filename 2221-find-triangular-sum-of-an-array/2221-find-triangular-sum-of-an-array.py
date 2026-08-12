class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        temp=nums[::]
        ans=[]
        while len(temp)!=1:

            for i in range(len(temp)-1):
                ans.append(sum(temp[i:i+2])%10)
            temp=ans[::]

            ans=[]
        return temp[0]

        
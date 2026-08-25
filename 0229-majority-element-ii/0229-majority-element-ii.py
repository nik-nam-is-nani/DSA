class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        mj=n//3
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        ans=[]
        for i,j in dic.items():
            if j>mj:
                ans.append(i)
        return ans

        
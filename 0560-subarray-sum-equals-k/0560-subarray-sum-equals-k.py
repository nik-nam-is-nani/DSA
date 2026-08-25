class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre=[]
        v=0
        d={}
        c=0
        d[0]=1
        for i in range(len(nums)):
            v+=nums[i]
            if v-k in d:
                c+=d[v-k]
            d[v]=d.get(v,0)+1


            
        return c

            

        

        
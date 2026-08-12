class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dic={}
        i=0
        j=0
        cn=0

        while j<len(nums):
            dic[nums[j]]=dic.get(nums[j],0)+1
            if dic.get(nums[j])<=k:
                cn=max(cn,j-i+1)
            while dic.get(nums[j])>k:
                dic[nums[i]]-=1
                i+=1
            j+=1
        
        return cn    

        
        
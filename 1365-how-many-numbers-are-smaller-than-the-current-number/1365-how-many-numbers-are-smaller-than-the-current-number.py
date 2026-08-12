class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        cn=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j] and i!=j:
                    cn+=1
            ans.append(cn)
            cn=0
        return ans

        
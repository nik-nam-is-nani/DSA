class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[]
        ans=[0]*len(nums)
        nve=1
        pve=0
        i=0
        while i<len(nums):
            if nums[i]>0:
                ans[pve]=nums[i]
                pve+=2
            else:
                ans[nve]=nums[i]
                nve+=2
            i+=1
        return ans

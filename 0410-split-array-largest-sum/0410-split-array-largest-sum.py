class Solution:
    def is_possible(self,nums,mid,k):
        s=1
        pgs=0
        for i in range(len(nums)):
            if pgs+nums[i]<=mid:
                pgs+=nums[i]
            else:
                s+=1
                pgs=nums[i]
        if s<=k:
            return False
        return True
    def splitArray(self, nums: List[int], k: int) -> int:
        ans=-1
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            if self.is_possible(nums,mid,k):
                low=mid+1
                ans=low
            else:
                high=mid-1
        return low

        
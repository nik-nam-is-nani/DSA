class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        mn=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                mn=min(mn,nums[low])
                low=mid+1
            elif nums[mid]<=nums[high]:
                mn=min(mn,nums[mid])
                high=mid-1
        return mn
        
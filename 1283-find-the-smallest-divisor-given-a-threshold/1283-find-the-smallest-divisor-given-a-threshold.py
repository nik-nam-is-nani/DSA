import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2

            sm=0
            for j in range(len(nums)):
                sm+=math.ceil(nums[j]/mid)
            if sm<=threshold:
                high=mid-1
                
            else:
                low=mid+1

        return low
                

        
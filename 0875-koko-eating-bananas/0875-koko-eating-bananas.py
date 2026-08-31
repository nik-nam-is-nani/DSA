import math
class Solution:
    def calcu(self,piles,hr):
        total=0
        for i in piles:
            total+=math.ceil(i/hr)
        return total
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            totalhr=self.calcu(piles,mid)
            if totalhr<=h:
                high=mid-1
            else:
                low=mid+1
        return low
        
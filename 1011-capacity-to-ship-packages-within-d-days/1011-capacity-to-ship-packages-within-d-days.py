class Solution:
    def check_days(self,mid,weights):
        day=1
        load=0
        for i in range(len(weights)):
            if load+weights[i]>mid:
                day+=1
                load=weights[i]
            else:
                load+=weights[i]
        return day





    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(high+low)//2
            no_D=self.check_days(mid,weights)
            if no_D<=days:
                high=mid-1
            else:
                low=mid+1
        return low

        
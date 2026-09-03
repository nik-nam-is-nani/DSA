class Solution:
    def is_possible(self,arr,day,m,k):
        nob=0
        cn=0
        for i in range(len(arr)):
            if arr[i]<=day:
                cn+=1
            else:
                nob+=(cn//k)
                cn=0
        nob+=(cn/k)
        if nob>=m:
            return True
        return False
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=min(bloomDay)
        high=max(bloomDay)
        # nums=bloomDay[::]
        # nums.sort()

        cn=0
        nob=0
        if k*m >len(bloomDay):
            return -1
        while low<=high:
            mid=(low+high)//2
            if self.is_possible(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return low


        #     else:
        #         high=
        #     for i in range(len(bloomDay)):
        #         if bloomDay[i]<nums[mid]:
        #             ans=mid
        #             high=mid-1
        #             break
        #         else:
        #             low=mid+1
        # return low

        
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        # if len(nums)==1:
        #     return k 
        nums=set(nums)
        low=1
        # nums.sort()
        # if nums[0]<k:
        #     low=nums[0]
        # else:
        #     low=k
        # if nums[-1]>k and k  not in nums:
        #     return k
        while low*k in nums:
            low+=1

        return low*k

        # low=nums[0]
        # high=nums[-1]
        # ans=-1
        # if low>k:
        #     return k
        # for i in range(1,high+1):
        #     if i*k not in nums:
        #         print(i*k)
        #         return i*k
        # return nums[-1]+k

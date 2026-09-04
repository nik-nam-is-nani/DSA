class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mx=max(nums)
        kval=float('inf')
        flg=False
        i=0
        while i<len(nums):
            mx=max(nums[:i+1])
            minval=min(nums[i:])
            # print("minval:",minval)
            # print("mx-minval:",mx-minval)
            # print("ival:",i)
            if mx-minval<=k:
                # print("minval:",minval)
                # print("mx-minval:",mx-minval)
                # print("ival:",i)
                kval=min(i,kval)
                flg=True
                print(kval)
                # break
            i+=1
        # for i in range(len(nums)):
        #     if mx-nums[i]>=k:
        #         kval=i
        #         flf=True
        if not flg:
            return -1
        return kval
        
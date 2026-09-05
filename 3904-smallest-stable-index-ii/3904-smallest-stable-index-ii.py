class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        pref_max = [0] * n
        current_max = nums[0]
        for i in range(n):
            current_max = max(current_max, nums[i])
            pref_max[i] = current_max
        suff_min = [0] * n
        current_min = nums[-1]
        for i in range(n - 1, -1, -1):
            current_min = min(current_min, nums[i])
            suff_min[i] = current_min
        for i in range(n):
            if pref_max[i] - suff_min[i] <= k:
                return i

        return -1

# class Solution:
#     def firstStableIndex(self, nums: list[int], k: int) -> int:
#         mx=max(nums)
#         kval=float('inf')
#         flg=False
#         i=0
#         while i<len(nums):
#             mx=max(nums[:i+1])
#             minval=min(nums[i:])
#             # print("minval:",minval)
#             # print("mx-minval:",mx-minval)
#             # print("ival:",i)
#             if mx-minval<=k:
#                 # print("minval:",minval)
#                 # print("mx-minval:",mx-minval)
#                 # print("ival:",i)
#                 kval=min(i,kval)
#                 flg=True
#                 print(kval)
#                 # break
#             i+=1
#         # for i in range(len(nums)):
#         #     if mx-nums[i]>=k:
#         #         kval=i
#         #         flf=True
#         if not flg:
#             return -1
#         return kval
        
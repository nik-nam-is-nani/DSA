class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rom=0
        for i in range(len(nums)):
            rom=nums[i]
            val=target-rom
            if val in nums and nums.index(val)!=i:

                return [i,nums.index(val)]
        return [-1,-1]
         

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        l=False
        r=len(nums)-1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                while nums[r]<=nums[i-1]:
                    r-=1
                nums[i-1],nums[r]=nums[r],nums[i-1]
                l=True
                break
        if l:
            nums[i:]=reversed(nums[i:])
        else:
            nums[:]=reversed(nums[:])










        
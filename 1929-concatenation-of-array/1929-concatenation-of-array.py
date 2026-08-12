class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=list(nums[::]+nums[::])

        return ans
        
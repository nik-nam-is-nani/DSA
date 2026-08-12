class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # count=0
        # maxval=0
        # mul=nums[0]
        # for i in range(1,len(nums)):
        #     mul*=nums[i]
        #     if mul==0:
        #         maxval=max(maxval,count)
        #         count=0
        #         mul=1
        #     count+=1
            
        # return maxval
        maxval=0
        i=0
        c=0
        while i <len(nums):
            if nums[i]==0:
                maxval=max(maxval,c)
                c=0
            elif nums[i]==1:
                c+=1
            i+=1
        maxval=max(maxval,c)
        return maxval
            




        
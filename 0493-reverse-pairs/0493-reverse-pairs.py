class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merg(nums, low, mid, high):
            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= high:
                temp.append(nums[right])
                right += 1

            for i in range(low, high + 1):
                nums[i] = temp[i - low]

        def count(nums, low, mid, high):
            right = mid + 1
            cn = 0

            for i in range(low, mid + 1):
                while right <= high and nums[i] > 2 * nums[right]:
                    right += 1

                cn += right - (mid + 1)

            return cn

        def mergeS(nums, low, high):
            if low >= high:
                return 0

            mid = (low + high) // 2

            left_count = mergeS(nums, low, mid)
            right_count = mergeS(nums, mid + 1, high)

            pair_count = count(nums, low, mid, high)

            merg(nums, low, mid, high)

            return left_count + right_count + pair_count

        return mergeS(nums, 0, len(nums) - 1)
# class Solution:
    # def reversePairs(self, nums: List[int]) -> int:
    #     cn=0
    #     def merg(self,nums,low,mid,high):
    #         temp=[]
    #         left,right=low,mid+1
    #         while left<=mid and right<=high:
    #             if nums[left]<=nums[right]:
    #                 temp.append(nums[left])
    #                 left+=1
    #             else:
    #                 temp.append(nums[right])
    #                 right+=1
    #         while left<=mid:
    #             temp.append(nums[left])
    #             left+=1
    #         while right<=high:
    #             temp.append(nums[right])
    #             right+=1
    #         for i in range(low,high+1):
    #             nums[i]=temp[i-low]
    #     def count(self,nums,low,mid,high):
    #         right=mid+1
    #         cn=0
    #         for i in range(low,mid+1):
    #             while right<high and nums[i]>(2*nums[right]):
    #                 right+=1
    #             cn+=(right-(mid+1))
    #         return cn
    #     def mergeS(self,nums,low,high):
    #         if low>=high:
    #             return 
    #         mid=(low+high)//2
    #         mergeS(nums,low,mid)
    #         mergeS(nums,mid+1,high)
    #         count(nums,low,mid,high)
    #         merg(nums,low,mid,high)
    #     self.mergeS(nums,0,len(nums)-1)
    #     return cn
        
        



                

        # cn=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>(nums[j]*2):
        #             cn+=1
        # return cn
        
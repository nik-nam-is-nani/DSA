class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        # Case 1: If the overall minimum is odd, we can always make every element odd.
        if min_val % 2 != 0:
            return True
        
        # Case 2: If the overall minimum is even, we cannot convert any odd numbers to even.
        # Thus, all elements must ALREADY be even.
        return all(x % 2 == 0 for x in nums1)

# class Solution:
#     def uniformArray(self, nums1: list[int]) -> bool:
#         if len(nums1) <= 2:
#             return True

#         val = abs(nums1[0] - nums1[1])

#         for i in range(1, len(nums1) - 1):
#             curr = abs(nums1[i] - nums1[i + 1])

#             if curr != val:
#                 return False

#         return True
# # class Solution:
#     def uniformArray(self, nums1: list[int]) -> bool:
#         if len(nums1)==1:
#             return True
#         nums2=[]
#         if nums1[0]%2==0:
#             num="even"
#         else:
#             num="odd"
#         nums2.append(nums1[0])
        
#         for i in range(1,len(nums1)):
#             if nums1[i]%2==0:
#                 s1="even"
#             else:
#                 s1="odd"
#             if s1==num:
#                 nums2.append(nums1[i])
#             else:
#                 return False
            
#                 # continue
#             # if nums1[i]-nums1[i+1] >=1:
#             #     val=nums1[i]-nums1[i+1]
#             #     if val%2==0:
#             #         valn="even"
#             #     else:
#             #         valn="odd"
#             #     if valn!=num:
#             #         return False
#             #     else:
#             #         nums2.append(val)
#         for i in range(len(nums1)-1):
#             val=abs(nums1[i]-nums1[i+1])
#             if val%2==0:
#                 valn="even"
#             else:
#                 valn="odd"
#             if valn!=num:
#                 return False
#                 # nums2.append(val)
#             #     # if len(nums2)==len(nums1):
#             #     #     return True
#             # else:
#             #     return False
            
#         return True




                        


# class Solution:
#     def uniformArray(self, nums1: list[int]) -> bool:
#         if len(nums1) == 1:
#             return True

#         nums2 = []

#         # Check parity of first element
#         if nums1[0] % 2 == 0:
#             num = "even"
#         else:
#             num = "odd"

#         nums2.append(nums1[0])

#         # Check whether all elements have same parity
#         for i in range(1, len(nums1)):
#             if nums1[i] % 2 == 0:
#                 s1 = "even"
#             else:
#                 s1 = "odd"

#             if s1 == num:
#                 nums2.append(nums1[i])
#             else:
#                 return False

#         # Check adjacent differences
#         for i in range(len(nums1) - 1):
#             val = abs(nums1[i] - nums1[i + 1])

#             if val % 2 == 0:
#                 valn = "even"
#             else:
#                 valn = "odd"

#             if valn != num:
#                 return False

#         return True

# class Solution:
#     def uniformArray(self, nums1: list[int]) -> bool:
#         if len(nums1) == 1:
#             return True

#         nums2 = []

#         if nums1[0] % 2 == 0:
#             num = "even"
#         else:
#             num = "odd"

#         nums2.append(nums1[0])

#         # Check differences between adjacent elements
#         for i in range(len(nums1) - 1):
#             val = abs(nums1[i] - nums1[i + 1])

#             if val % 2 == 0:
#                 valn = "even"
#             else:
#                 valn = "odd"

#             if valn == num:
#                 nums2.append(val)
#             else:
#                 return False

#         return True
        
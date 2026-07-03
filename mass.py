# nums = [9,0]
# target = 9
# temp=0
# for i in range(len(nums)):
#     temp=nums[i]
#     if abs(temp-target) in nums:
#         print([i,nums.index(abs(temp-target))])
# print([-1,-1])


        
# for i in range(len(nums)):#2,7,11,15
#         for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                         print([i,j])
# print([-1,-1])


# c=a+b
# if c==target:
#     return [a,b]
# 2+7
# 2+11
# 2+15
# 7+11
x=121
# print(str(x)[::-1])
if x<0:
    print("not")
elif str(x)[::]==str(x)[::-1]:
    print("yes")
else:
    print("no")

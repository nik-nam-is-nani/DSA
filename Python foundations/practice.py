

# # from continue number addition code 
# n=1234
# sum=0
# for i in str(n):
#     sum+=int(i)
# print(sum)
# print("====================================")
# #====================================



# #Reverse a Number
# print("Reverse a Number")

# n=1234
# print("before: ",n)
# p=[]
# while n:
#     d=n%10
#     n=n//10
#     p.append(str(d))
# d="".join(p)

# print(d)
# print("============================\n========================")
# print("==============================================Longest Substring Without Repeating Characters=============================")

# n="asdfghjklmnvcmnvmnvmnvmncvmn"
# seen=set()
# left=0
# max_len=0
# for right in range(len(n)):
#     while n[right] in seen:
#         seen.remove(n[left])
#         left+=1
#     seen.add(n[right])
#     max_len=max(max_len,right-left+1)
# print(max_len)



# #=======================================================
# n="asdfghjklmnvcmnvmnvmnvmncvmn"
# seen=set()
# left=0
# max_len=0
# Start=0
# for right in range(len(n)):
#     while n[right] in seen:
#         seen.remove(n[left])
#         left+=1
#     seen.add(n[right])
#     if right-left+1>max_len:
#         max_len=right-left+1
#         Start=left
# print(n[Start:max_len])
# print(max_len)
# print("========================================================")
# #=======================================
# print(" Reverse Words in a String III")
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         op=s.split()
#         va=""
#         for i in range(len(op)):
#             op[i]=op[i][::-1]
          
#         return " ".join(op)
# print("=====================================")

# val="1 23 34 56"
# va=list(map(int,val.split()))
# print(va)

# x=int(1234)
# x=str(x)
# x=x[::-1]
# print(x)
# n=14
# print("mass :",n & n-1)
# print(n & (n-1)==0)
# n=12
# i=1
# a="11"
# b="1"
# print("new")




# a1=int(a,2)
# b1=int(b,2)
# a1=a1+b1
# a1=bin(a1)
# a1=a1[2:]
# a1=str(a1)
# print(a1)
        

# res="4"==4

# # print(res)
# # mass="abs23"
# # print(any(mass.isalpha()))

# # class Solution:
# #     def maximumValue(self, strs: List[str]) -> int:
# #         max_val = 0
# #         for s in strs:
# #             max_val = max(self.get_value(s), max_val)
# #         return max_val
# #     def get_value(self,s:str):
# #         for idx, c in enumerate(s):
# #             if c.isalpha():
# #                 return len(s)

# a="K"
# c="d"
# b=ord(a)+1
# print(f"{chr(b)}{c}")

# names = ["Mary","John","Emma"]
# heights = [180,165,170]

# sor=sorted(heights,reverse=True)
# res=[]
# for i in range(len(sor)):
#     res.append(names[heights.index(sor[i])])
#     print(res)





# peo = [
#     ["nik", 21],
#     ["ram", 18],
#     ["sai", 25]
# ]

# peo.sort(key=lambda x:x[1], reverse=True)


# #used  when we are implementing the zip funticons in the dsa 
# startTime = [1,2,3]
# endTime = [3,2,7]
# queryTime = 4
# c=0
# for i in range(len(startTime)):
#     if startTime[i]-endTime[i]==queryTime:
#         c+=1
#     print(startTime[i]-endTime[i])
# s="aaba"


# le=len(s)-1
# i=0
# b=False
# a=False
# while i<=le:
#     print("val B ",b)
#     print("val A ",a)
#     if s[i]=='a' and b==False:
#         a=True
#         i+=1
#     elif s[i]=='b':
#         print("massssss")
#         b=True
#         i+=1
#     else:
#         print(False)
#         i+=1
# print(True)

# nums =[87063,61094,44530,21297,95857,93551,9918]
# ans=[]
# le=len(nums)
# mx=float('-inf')
# mn=float('inf')
# for i in range(le):
#     for j in range(le):
#         if j!=i:
#             mx=max(mx,abs(nums[j]))
#             mn=min(mn,abs(nums[j]))
#     ans.append(mx-mn)
# # return ans

# # class Solution:
# #     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
# #         res = [[0] * c for _ in range(r)]
# #         n, m = 0, 0
# #         if (len(mat)*len(mat[0])) != r*c:
# #             return mat
# #         for i in range(len(mat)):
# #             for j in range(len(mat[0])):
# #                 res[n][m] = mat[i][j]
# #                 m += 1
# #                 if m >= c:
# #                     n+=1
# #                     m = 0
# #         return res

# print(chr(97))

# print(ord('P'))
# n=[2,4,6,8,10]
# ans=[]
# ans.append(n[0])
# for i in range(1,len(n)):
    
#     ans.append(ans[i-1]+n[i])
# print(ans)
# n=[2,4,6,8,10]
# let=[]
# ans=[]

# right=[0]*(len(n)-1)
# right.append(1)
# let.append(1)
# for i in range(1,len(n)):
#     let.append(let[i-1]*n[i-1])
#     right[n-i]=right[n-i+1]*n[n-i+1]
# for i in range(len(n)):
#     ans.append(let[i]*right[i])
# print(ans)
# print(chr(0+97))
# print(ord('z'))


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# a=intervals[1]
# print(a[1])
# print(sorted(intervals))
# invervals=sorted(intervals)
# ans=[]
# # for i in range(len(intervals)):
# #     if intervals[i][1]>intervals[i+1][0]:
# #         ans.append([invervals[i][0],intervals[i+1][1]])
# #     else:
# #         ans.append([intervals[i]])
# print(ans)  
# nums = [3,30,34,5,9]
# print(nums[2])
# ans=[8,6,4,65,7,78]
# v="".join(map(str,ans))
# # print(v)
# nums=[222]
# # ans=str(ans)
# # # print(str(nums[0]))
# # # print("".join(ans))

# print( )
words = ["aba","aabb","abcd","bac","aabc"]
# ans=[]
# for i in words:
#     ans.append("".join(set(i)))
# print(words)
# print(ans)
# from collections import Counter
# words_counter = Counter()
# total_pairs = 0
# for word in words:
#     tuple_of_word = tuple(set(word))
#     print(tuple_of_word)
#     words_counter[tuple_of_word] += 1 
# print(words_counter)
# pairs = 0
# for key, value in words_counter.items():
#     if value > 1:
#         print(value)
#         pairs += (value * (value - 1)) // 2
# print(pairs)
# s="belll"
# m="bel"
# print(s-m)
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
dic=[]
c=0
for i in allowed:
    dic.append(i)
for i in words:
    print(set(i),set(allowed))
    if set(i)<= set(allowed):
        c+=1
print(c)

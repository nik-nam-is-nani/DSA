

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
# allowed = "abc"
# words = ["a","b","c","ab","ac","bc","abc"]
# dic=[]
# c=0
# for i in allowed:
#     dic.append(i)
# for i in words:
#     print(set(i),set(allowed))
#     if set(i)<= set(allowed):
#         c+=1
# print(c)
# nums = [0,1,2,2,4,4,4,1]
# ans={}
# ans1=[]
# for i in range(len(nums)):
#     if nums[i] not in ans:
#         ans[nums[i]]=1
#     else:
#         ans[nums[i]]+=1
# for key,val in ans.items():
#     if key%2==0:
#         ans1.append(key)
# ans1.sort()
# print(ans1)
# m=0
# for i in range(len(ans1)):
#     m=max(m,ans1[i])
# print(m)  
# 
from collections import Counter
# nums = [0,1,2,0,0,0,2,4,4,1]  
# nums=[i for i in nums if i %2==0]
# ans = dict(sorted(Counter(i for i in nums if i % 2 == 0).items()))
# print(ans)
# v1=0
# key=0
# for i,j in ans.items():
#     if v1<j:
#         v1=j
#         key=i
# print(key)

# v1=ans[max(ans)]
# print(v1)
# for i,j in ans.items():
#     if v1==j:
#         print(i)
#         break
# print(ans)
# print(ans[max(ans)])
# ans1=[]
# for i in range(len(nums)):
#     if nums[i] not in ans and nums[i]%2==0:
#         ans[nums[i]]=1
#     elif nums[i]%2==0:
#         ans[nums[i]]+=1
# print(ans)
# m=0
# for i in range(len(ans)):
#     m=max(m,ans[i])
# print(m)
# s = "Aabbcccddeeee"
# co=Counter(s)
# for i,j in co.items():
#     print(i)

# print(co)
# ans=dict(sorted(co.items(),key=lambda x: x[1],reverse=True))
# for i,j in ans.items():
#     print(i*j,end="")

# arr = ["d","b","c","b","c","a"]
# k = 2
# print(Counter(arr))
# s = "Hello how are you Contestant"
# ans=s.split()
# print(ans)
# print(chr(ord('a')+int('1')))
# words = ["abc","car","ada","racecar","cool"]
# for i in words:
#     if i[::]==i[::-1]:
#         print(i)
# ans=[]
# word = "abcdefd"
# ch="d"
# for i in range(len(word)):
#     if word[i]==ch:
#         # print(word[:-i])
# print(word[::-3])
# for i in range(ord('a'),ord('z')+1):
#     print(chr(i),end=" ")
# s = "textbook"
# a=Counter(s[:len(s)//2])
# b=Counter(s[len(s)//2:])
# print(a)
# print(b)
# ove=['a','e','i','o','u','A','E','I','O','U']
# o=[i for i in b if i in ove]
# o1=[i for i in a if i in ove]
# ans1=0
# ans2=0
# print(o)
# for i in b:
#     ans1+=b[i]
# for i in a:
#     ans2+=a[i]
# print(ans1==ans2)
# s = "abab"
# # s=str(s[::])
# p = "ab"
# print('8*88*********888')
# print(s)
# print(sorted(p))
# p=sorted(p)
# print(p)
# k=len(p)
# ans=[]
# print(p)
# che=[]

# p=sum(ord(p[::]))
# print(p)
# for i in range(len(s)):
    # print(str(s[i:i+k]))
    # print(p)
    # print(i)
    # print(sorted(s[i:i+k]))
    # print(list(s[i:i+k]))
#     if str(s[i:i+k]) == sum():
#         ans.append(i)
# print(ans)
# s = "abab"
# p = "ab"

# psum=0
# for i in p:
#     psum+=ord(i)
# p1=[]
# p1.append(ord(s[0]))
# for i in range(1,len(s)):
#     p1.append(ord(s[i])+p1[i-1])
# print(p1)
# anop=[]
# i=0
# j=i+len(p)

# while j<len(p1):
#     if p1[j]-p1[i] ==psum:
#         anop.append(i+1)
#     # anop.append(p1[j]-p1[i])
#     j+=1
#     i+=1
# # anop.append()
# print(anop)
# pan=[]



# psum=0
# for i in p:
#     psum+=ord(i)
# p1=[]
# p1.append(ord(s[0]))
# for i in range(1,len(s)):
#     p1.append(ord(s[i])+p1[i-1])
# print(p1)
# anop=[]
# i=0
# j=i+len(p)
# while j<len(p1):
#     print(p1[j])
#     if p1[i]==psum:
#         anop.insert(0,0)
#         print(anop)
#     if p1[j]-p1[i] ==psum:
#         anop.append(i+1)
#         print(anop)
#     # anop.append(p1[j]-p1[i])
#     j+=1
#     i+=1
# # anop.append()
# print(anop)



# print(psum)
# ans=[]
# t=0
# a=0
# for i in range(len(s)):
#     if t<len(p):
#         a+=ord(s[i])
#         print(a)
#         t+=1
#     else:
#         ans.append(a)
#         t=0
#         a=0
# print(ans)
# a=list(map(int,input().split()))
# print(a[::-1])
# print(ord('A'))
# print(ord('a'))
# print(ord('Z'))
# print(ord('z'))
# print(chr(91))
# arr = [1,0,2,3,0,4,5,0]
# ans=[]
# for i in arr:
#     if i==0:
#         ans.append(i)
#         ans.append(0)
#     else:
#         ans.append(i)
# # print(ans[:len(arr)])
s = "ab#c"
t = "ad#c"
# i=len(s)-1
# j=len(t)-1
# c1=0
# c2=0
# while i:
#     print(s[i])
#     if s[i]=='#':
#         c1+=1
#         s.pop(i)
#     else:
#         while c1:
#             s.pop(i)
#             c1-=1
#     i-=1
# while j:
#     if t[j]=="#":
#         c2+=1
#         t.pop(j)
#     else:
#         while c2:
#             t.pop(j)
#             c2-=1
#     j-=1
# a=[i for i in s]
# print(a)
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# dic={'+','-','*','/'}
# ans=0
# temp=list(tokens)
# te1=[]
# for i in temp:
#     if i in dic:
#         if i=='+':
#             ans+=int(te1.pop())+int(te1.pop())
#             print(ans)
#             te1.append(ans)
#             ans=0
#             print(te1)
#         elif i=='-':
#             ans+=int(te1.pop())-int(te1.pop())
#             print(ans)
#             te1.append(ans)
#             ans=0
#             print(te1)
#         elif i=='*':
#             ans+=int(te1.pop())*int(te1.pop())
#             print(ans)
#             te1.append(ans)
#             ans=0
#             print(te1)
#         elif i=='/':
#             ans+=int(te1.pop())/int(te1.pop())
#             print(ans)
#             te1.append(ans)
#             ans=0
#             print(te1)
#     else:
#         te1.append(i)
#         print(ans)
#         print(te1)
# # return ans
# print(ans)
# print(te1)
# nums = [1,2,3,4,3]
# ans=[]
# for i in range(len(nums)):

#     j=i
#     flag=False
#     print(i,j)
#     while j<len(nums) and nums[i]>=nums[j]:
#         if j+1<len(nums):
#             j+=1
#         flag=True
#     if flag:
#         ans.append(nums[j])
#         flag=False
#     else:
#         ans.append(-1)
# print(ans)
# class mass:
#     def decorator(func):

#         def wrapper():
#             print("Starting...")

#             func()

#             print("Ending...")

#         return wrapper
#     gr=decorator(gr)
#     gr()
#=================================================================




# n=6
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range((2*i)+1):
#         print("*",end="")
#     for j in range(n-i-1):
#         print(" ",end="")
#         # print(" "*(n-i-1),end="")
#         # print("*"*((2*i)+1),end="")
#         # print(" "*(n-i-1),end="")
#     print("")
#=========================================================================
# n=int(input())
# for i in range(n):
#     for j in range(i):
#         print("*",end="")
#     print("")
# for i in range(n-2,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("")


# n=20
# a=0
# b=1
# a_chance=True
# b_ch=False
# firs=True

# for i in range(n-1,0,-1):
#     for j in range(i):
#         if i%2==0:
#             print((j+1)%2,end="")
#         else:
#             print(j%2,end="")
#     print("")

    #     if firs:
    #         if a_chance:
    #             print(a,end="")
    #             a_chance=False
    #             b_ch=True

    #         else:
    #             print(b,end="")
    #             b_ch=False
    #             a_chance=True
    #         firs=False
    #     else:
    #         if a_chance:
    #                 print(b,end="")
    #                 a_chance=True
    #                 b_ch=False

    #         else:
    #             print(a,end="")
    #             b_ch=True
    #             a_chance=False
    #         firs=True

    # print("")
#=============================================================

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
#     val=n+n-i-i
#     for j in range(val-2):

#         print(" ",end="")
#     for j in range(i+1,0,-1):
#         print(j,end="")
#     print()
#===================================================


# n=6
# i=1
# for j in range(n+1):
#     for k in range(j):
#         print(i,end=" ")
#         i+=1
#     print()
#==========================================================================
# a='A'
# n=5
# for i in range(n):
#     for j in range(i):
#         print(chr(ord(a)+i),end="")
#     print() 
#=========================================================================
# n=5
# i=n-1
# while (n*2)-1>0:
#     n=n-1
#     i=n
#     while i:
#         print(i,end="")
#         i-=1
#     print()
# n=4
# for i in range(1,n+1,1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print(i,end="")
#     for j in range(n-i):
#         print(" ",end="")
#     print()
# n=5
        
# for i in range(2 * n - 1):
#     for j in range(2 * n - 1):
#         top = i
#         # print("iteration :",i)
#         # print("innner iteration: ",j)
#         # print("top:",top)
#         left = j
#         # print("left:",left)
#         bottom = (2 * n - 2) - i
#         right = (2 * n - 2) - j
#         # print("bottom: ",bottom)
#         # print("right: ",right)

#         minDist = min(top, bottom, left, right)
#         # print("==============================================")

#         print(n - minDist, end=" ")
#         # print("==============================================")

#     print()
#==========================================================================

# n=5
# for i in range(n):
#     ch='E'
#     for j in range(ord(ch)-i,ord('E')+1,1):
#         print(chr(j),end=" ")
#     print()
#============================================================================
# n=5

# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     for j in range(i+i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*",end="")
#     print()
# for i in range(n-1,-1,-1):
#     for j in range(n-i):
#         print("*",end="")
#     for j in range(i+i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*",end="")
#     print()

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
#=========================================================================================
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==n-1 or j==0  and i!=0 and i!=n-1:
#             print("*",end=" ")
#         elif i==0 or i==n-1:
#             print("*",end=" ")
        
#         else:
#             print(" ",end=" ")
#     print()
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 
#======================================================
# arr=[1,2,3,4,5,3,6,7,8,0,77,98,67]
# larger=-1
# for i in range(len(arr)):
#     if arr[i]>larger:
#         larger=arr[i]
# sec=-1
# for i in range(len(arr)):
#     if arr[i]>sec and arr[i]!=larger:
#         sec=arr[i]

# print(sec)
# lrg=arr[0]
# sec_min=float('-inf')
# for j in range(1,len(arr)):
#     if lrg<arr[j]:
#         sec_min=lrg
#         lrg=arr[j]
# print(sec_min)
#=====================================================================================
# sor_arr=[1,2,3,3,4,5,6,7,7,8,8,9,9,10,10,11,11]
# se=list(set(sor_arr))
# for i in range(len(se)):\\one Aproach 
#     sor_arr[i]=se[i]
# print(sor_arr)
# i=0
# for j in range(1,len(sor_arr)):    \\ optimal aproch of this thing 
#     if sor_arr[i]!=sor_arr[j]:
#         sor_arr[i+1]=sor_arr[j]
#         i+=1
# print(sor_arr)
#================================================================
arr1=[1,1,2,3,4,5]
arr2=[2,3,4,4,5,6]
se=list(set(arr1))
se.extend(list(set(arr2)))
se=list(set(se))
se.sort()


print(se)


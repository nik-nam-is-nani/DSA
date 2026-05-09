

# from continue number addition code 
n=1234
sum=0
for i in str(n):
    sum+=int(i)
print(sum)
print("====================================")
#====================================



#Reverse a Number
print("Reverse a Number")

n=1234
print("before: ",n)
p=[]
while n:
    d=n%10
    n=n//10
    p.append(str(d))
d="".join(p)

print(d)
print("============================\n========================")
print("==============================================Longest Substring Without Repeating Characters=============================")

n="asdfghjklmnvcmnvmnvmnvmncvmn"
seen=set()
left=0
max_len=0
for right in range(len(n)):
    while n[right] in seen:
        seen.remove(n[left])
        left+=1
    seen.add(n[right])
    max_len=max(max_len,right-left+1)
print(max_len)



#=======================================================
n="asdfghjklmnvcmnvmnvmnvmncvmn"
seen=set()
left=0
max_len=0
Start=0
for right in range(len(n)):
    while n[right] in seen:
        seen.remove(n[left])
        left+=1
    seen.add(n[right])
    if right-left+1>max_len:
        max_len=right-left+1
        Start=left
print(n[Start:max_len])
print(max_len)
print("========================================================")
#=======================================
print(" Reverse Words in a String III")
class Solution:
    def reverseWords(self, s: str) -> str:
        op=s.split()
        va=""
        for i in range(len(op)):
            op[i]=op[i][::-1]
          
        return " ".join(op)
print("=====================================")

val="1 23 34 56"
va=list(map(int,val.split()))
print(va)

x=int(1234)
x=str(x)
x=x[::-1]
print(x)
n=14
print("mass :",n & n-1)
print(n & (n-1)==0)
n=12
i=1
a="11"
b="1"
print("new")




a1=int(a,2)
b1=int(b,2)
a1=a1+b1
a1=bin(a1)
a1=a1[2:]
a1=str(a1)
print(a1)
        

res="4"==4

# print(res)
# mass="abs23"
# print(any(mass.isalpha()))

# class Solution:
#     def maximumValue(self, strs: List[str]) -> int:
#         max_val = 0
#         for s in strs:
#             max_val = max(self.get_value(s), max_val)
#         return max_val
#     def get_value(self,s:str):
#         for idx, c in enumerate(s):
#             if c.isalpha():
#                 return len(s)

a="K"
c="d"
b=ord(a)+1
print(f"{chr(b)}{c}")


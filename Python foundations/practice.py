

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
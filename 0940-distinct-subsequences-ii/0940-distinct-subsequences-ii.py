class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1
        last = {}

        for ch in s:
            new_dp = (dp * 2) % MOD

            if ch in last:
                new_dp = (new_dp - last[ch]) % MOD

            last[ch] = dp
            dp = new_dp

        return (dp - 1) % MOD
# class Solution:
#     def goo(self, i, se, v, s):
#         if i == len(s):
#             se.add("".join(v))
#             return
#         v.append(s[i])
#         self.goo(i + 1, se, v, s)
#         v.pop()
#         self.goo(i + 1, se, v, s)
#     def distinctSubseqII(self, s: str) -> int:
#         se = set()
#         v = []
#         self.goo(0, se, v, s)
#         return len(se) - 1
#     se=set()
#     v=[]
#     v.append(str(0))
#     def goo(self,i,se,s):
#         if i>len(s):
#             return
#         self.v.append(s[i])
        
#         self.se.add("".join(self.v))
#         self.goo(i+1,self.se,s)
#         self.v.pop()
#         self.goo(i+1,self.se,s)


#     def distinctSubseqII(self, s: str) -> int:
#         i=0
#         self.goo(i,self.se,s)
#         return len(self.se)
        
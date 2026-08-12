class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        for ch in count:
            if count[ch]<k:
                parts=s.split(ch)
                ans=0
                for part in parts:
                    ans=max(ans,self.longestSubstring(part,k))
                return ans

        return len(s)
            
        
















        # dic={}
        # i=0
        # j=0
        # cn=0
        # flag=False

        # while j<len(s):
        #     dic[s[j]]=dic.get(s[j],0)+1

        #     # while dic.get(s[j])<k:
        #     #     dic[s[i]]-=1
        #     #     i+=1
        #     j+=1
        # for i,j in dic.items():
        #     if j>=k:
        #         flag=True
        #     else:
        #         flag=False
        # if flag:
        #     return len(s)
        # else:


        
        # while 
        #     if dic.get(s[j])>=k:
        #         cn=max(cn,j-i+1)
        # i=0

        

        
        # return cn    
        
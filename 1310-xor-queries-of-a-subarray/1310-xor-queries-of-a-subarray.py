class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        s=0
        prefix=[0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)
        for i,j in queries:
            s=0
            ans.append(prefix[j+1]^prefix[i])
        return ans
        
class Solution:
    def reverseDegree(self, s: str) -> int:
        sm=0
        for i in range(len(s)):
            sm+=(ord('z')-ord(s[i])+1)*(i+1)
            # print(ord('z')-ord(s[i])+1)

            print(sm)
        return sm
        
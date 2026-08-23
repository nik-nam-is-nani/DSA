class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic={}
        used=set()
        wor=s.split()
        if len(pattern)!=len(wor):
            return False

        for i,j in zip(pattern,s.split()):
            if i in dic:
                if dic[i]!=j:
                    return False
            else:
                if j in used:
                    return False
                dic[i]=j
                used.add(j)
            # if i not in dic and j not in dic:
            #     dic[i]=j
            # elif dic[i]!=j:
            #     return False
        return True

        
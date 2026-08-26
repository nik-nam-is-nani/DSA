class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        re=[]
        for i in range(len(rocks)):
            re.append(capacity[i]-rocks[i])
        re.sort()
        for i in range(len(re)):

            if re[i]==0:
                continue
            if additionalRocks>=re[i]:
                additionalRocks-=re[i]
                re[i]=0

        cn=0
        for i in range(len(re)):
            if re[i]==0:
                cn+=1
        return cn
            


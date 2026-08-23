class Solution:
    def reverseBits(self, n: int) -> int:
        val=bin(n)[2:]
        
        val=val[::-1]
        for i in range(len(val),32):
            val+=str(0)
        return int(val,2)

        # return (int(val[::-1],2))

        
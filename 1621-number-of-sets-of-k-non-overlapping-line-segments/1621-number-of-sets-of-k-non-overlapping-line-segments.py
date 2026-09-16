class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        def mod_pow(a, b):
            res = 1
            while b:
                if b & 1:
                    res = res * a % MOD
                a = a * a % MOD
                b >>= 1
            return res

        r = 2 * k
        num = 1
        den = 1

        for i in range(1, r + 1):
            num = num * (n + k - i) % MOD
            den = den * i % MOD

        return num * mod_pow(den, MOD - 2) % MOD
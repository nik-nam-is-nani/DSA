class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = [0] * 10

        for d in digits:
            cnt[d] += 1

        ans = 0

        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            used = [0] * 10
            used[a] += 1
            used[b] += 1
            used[c] += 1

            if all(used[d] <= cnt[d] for d in range(10)):
                ans += 1

        return ans
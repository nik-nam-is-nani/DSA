from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:

        n = len(nums)
        size = 1

        while size < n:
            size *= 2

        total = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        for i in range(n):
            r = nums[i] % k
            total[size + i] = r
            cnt[size + i][r] = 1

        def merge(left, right):
            lt, lc = left
            rt, rc = right

            result = lc[:]

            for r in range(k):
                if rc[r]:
                    new_r = (lt * r) % k
                    result[new_r] += rc[r]

            return ((lt * rt) % k, result)

        for i in range(size - 1, 0, -1):
            total[i], cnt[i] = merge(
                (total[i * 2], cnt[i * 2]),
                (total[i * 2 + 1], cnt[i * 2 + 1])
            )

        def update(pos, value):
            pos += size

            r = value % k

            total[pos] = r
            cnt[pos] = [0] * k
            cnt[pos][r] = 1

            pos //= 2

            while pos:
                total[pos], cnt[pos] = merge(
                    (total[pos * 2], cnt[pos * 2]),
                    (total[pos * 2 + 1], cnt[pos * 2 + 1])
                )

                pos //= 2

        def query(l, r):
            left_result = (1, [0] * k)
            right_result = (1, [0] * k)

            l += size
            r += size

            while l <= r:

                if l % 2 == 1:
                    left_result = merge(
                        left_result,
                        (total[l], cnt[l])
                    )
                    l += 1

                if r % 2 == 0:
                    right_result = merge(
                        (total[r], cnt[r]),
                        right_result
                    )
                    r -= 1

                l //= 2
                r //= 2

            return merge(left_result, right_result)

        result = []

        for index, value, start, x in queries:

            update(index, value)

            _, counts = query(start, n - 1)

            result.append(counts[x])

        return result
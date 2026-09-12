from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        a = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        # Sort by ending position
        a.sort(key=lambda x: x[1])

        ends = [x[1] for x in a]

        # dp[k][i] = (maximum weight, chosen indices)
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for i in range(1, n + 1):
            l, r, w, idx = a[i - 1]

            # intervals ending < l
            p = bisect_left(ends, l, 0, i - 1)

            for k in range(1, 5):
                skip = dp[k][i - 1]

                take_weight = dp[k - 1][p][0] + w
                take_indices = tuple(sorted(dp[k - 1][p][1] + (idx,)))
                take = (take_weight, take_indices)

                if take[0] > skip[0] or (
                    take[0] == skip[0] and take[1] < skip[1]
                ):
                    dp[k][i] = take
                else:
                    dp[k][i] = skip

        ans = (0, ())

        for k in range(1, 5):
            cur = dp[k][n]

            if cur[0] > ans[0] or (
                cur[0] == ans[0] and cur[1] < ans[1]
            ):
                ans = cur

        return list(ans[1])
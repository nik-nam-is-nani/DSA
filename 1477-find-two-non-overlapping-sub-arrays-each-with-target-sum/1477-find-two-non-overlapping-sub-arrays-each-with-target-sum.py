class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        ans = float('inf')
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0:
                    ans = min(ans, length + best[left - 1])

                min_len = min(min_len, length)

            best[right] = min_len

        return ans if ans != float('inf') else -1
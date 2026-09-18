class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            x = ord(c) - 97
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for i in range(26):
            if first[i] == n:
                continue

            l, r = first[i], last[i]
            j = l
            valid = True

            while j <= r:
                x = ord(s[j]) - 97

                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                j += 1

            if valid:
                intervals.append((r, l))

        intervals.sort()

        result = []
        prev = -1

        for r, l in intervals:
            if l > prev:
                result.append(s[l:r + 1])
                prev = r

        return result
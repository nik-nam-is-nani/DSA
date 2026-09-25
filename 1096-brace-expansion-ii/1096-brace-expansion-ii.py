class Solution:
    def braceExpansionII(self, expression):
        n = len(expression)

        def parse(i):
            result = set()
            current = {""}

            while i < n and expression[i] != '}':
                if expression[i] == '{':
                    part, i = parse(i + 1)

                elif expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                    continue

                else:
                    part = {expression[i]}
                    i += 1

                current = {a + b for a in current for b in part}

            result |= current

            if i < n and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)
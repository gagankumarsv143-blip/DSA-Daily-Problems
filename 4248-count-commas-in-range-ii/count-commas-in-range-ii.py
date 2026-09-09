class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        if n >= 1000:
            end = min(n, 999999)
            ans += end - 1000 + 1

        if n >= 1000000:
            end = min(n, 999999999)
            ans += (end - 1000000 + 1) * 2

        if n >= 1000000000:
            end = min(n, 999999999999)
            ans += (end - 1000000000 + 1) * 3

        if n >= 1000000000000:
            end = min(n, 999999999999999)
            ans += (end - 1000000000000 + 1) * 4

        if n >= 1000000000000000:
            ans += (n - 1000000000000000 + 1) * 5

        return ans
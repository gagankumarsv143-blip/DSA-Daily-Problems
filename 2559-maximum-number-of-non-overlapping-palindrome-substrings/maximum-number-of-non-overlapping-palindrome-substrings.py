class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if length == 1:
                    pal[l][r] = True

                elif length == 2:
                    pal[l][r] = (s[l] == s[r])

                else:
                    pal[l][r] = (s[l] == s[r] and pal[l + 1][r - 1])

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            for j in range(i):
                length = i - j

                if length >= k and pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        if n == 1:
            return 0

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] = maximum score from l to r
        dp = [[0] * n for _ in range(n)]

        # For every l:
        # split[l] = first position where
        # left_sum >= right_sum
        split = [0] * n

        # Best value of:
        # dp[l][k] + left_sum
        # for all k where left_sum < right_sum
        left_best = [float("-inf")] * n

        for r in range(1, n):

            # suffix[k] =
            # max(dp[k+1][r] - prefix[k+1])
            suffix = [float("-inf")] * (r + 1)

            # l must go backwards because
            # dp[l+1][r] must already be calculated.
            for l in range(r - 1, -1, -1):

                # Add split k = l
                value = dp[l + 1][r] - prefix[l + 1]

                suffix[l] = max(value, suffix[l + 1])

                # Make sure split starts at l
                if split[l] < l:
                    split[l] = l

                # Move split while:
                # left_sum < right_sum
                while split[l] < r:

                    k = split[l]

                    left_sum = prefix[k + 1] - prefix[l]
                    right_sum = prefix[r + 1] - prefix[k + 1]

                    if left_sum < right_sum:

                        left_best[l] = max(
                            left_best[l],
                            dp[l][k] + left_sum
                        )

                        split[l] += 1

                    else:
                        break

                best = left_best[l]

                # There is a split where
                # left_sum >= right_sum
                if split[l] < r:

                    k = split[l]

                    left_sum = prefix[k + 1] - prefix[l]
                    right_sum = prefix[r + 1] - prefix[k + 1]

                    # Right side is chosen
                    best = max(
                        best,
                        prefix[r + 1] + suffix[k]
                    )

                    # Equal sums -> Alice can choose either side
                    if left_sum == right_sum:
                        best = max(
                            best,
                            left_sum + dp[l][k]
                        )

                dp[l][r] = best

        return dp[0][n - 1]
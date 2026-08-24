from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        n = len(stones)

        # Prefix sum
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # At the end, Alice must take all stones.
        # This is the starting best score difference.
        ans = prefix[n - 1]

        # Work backwards.
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans
from functools import lru_cache
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0

            best = float("-inf")
            total = 0

            for j in range(3):
                if i + j < n:
                    total += stoneValue[i + j]
                    best = max(best, total - dp(i + j + 1))

            return best

        score = dp(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"
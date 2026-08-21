from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            """
            Number of distinct amounts <= x
            that can be made using at least one coin.
            """

            total = 0
            n = len(coins)

            # Inclusion-exclusion
            for mask in range(1, 1 << n):

                multiple = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        multiple = lcm(multiple, coins[i])
                        bits += 1

                        # No multiples <= x
                        if multiple > x:
                            break

                if multiple > x:
                    continue

                value = x // multiple

                if bits % 2 == 1:
                    total += value
                else:
                    total -= value

            return total

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:

            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
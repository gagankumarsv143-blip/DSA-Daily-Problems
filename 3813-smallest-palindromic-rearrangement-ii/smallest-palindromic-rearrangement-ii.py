from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = {}
        mid = ""

        for ch in sorted(freq):
            half[ch] = freq[ch] // 2
            if freq[ch] % 2:
                mid = ch

        m = sum(half.values())

        def count_perm(cnt):
            total = sum(cnt.values())
            ans = 1
            rem = total
            for v in cnt.values():
                if v:
                    ans *= comb(rem, v)
                    rem -= v
                    if ans > k:
                        return ans
            return ans

        if count_perm(half) < k:
            return ""

        left = []

        while m:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = count_perm(half)

                if ways >= k:
                    left.append(ch)
                    m -= 1
                    break
                else:
                    k -= ways
                    half[ch] += 1

        left = "".join(left)
        return left + mid + left[::-1]
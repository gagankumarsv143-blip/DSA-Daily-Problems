from typing import *

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check whether palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Characters available for left half
        half = [0] * 26
        for i in range(26):
            half[i] = count[i] // 2

        m = n // 2

        # We only need the first half of target
        target_half = target[:m]

        # Try to build the smallest half >= target_half
        ans = []

        for i in range(m):
            t = ord(target_half[i]) - ord('a')

            # Try to use target character if possible
            if half[t] > 0:
                ans.append(target_half[i])
                half[t] -= 1
                continue

            # Cannot match target.
            # Find the smallest character greater than target[i]
            bigger = -1

            for c in range(t + 1, 26):
                if half[c] > 0:
                    bigger = c
                    break

            if bigger != -1:
                ans.append(chr(bigger + ord('a')))
                half[bigger] -= 1

                # Fill remaining positions with smallest characters
                rest = []

                for c in range(26):
                    rest.extend([chr(c + ord('a'))] * half[c])

                left = ''.join(ans) + ''.join(rest)

                right = left[::-1]

                return left + middle + right

            # No bigger character here.
            # We need to backtrack.
            break

        else:
            # We matched target's first half completely.
            left = ''.join(ans)

            palindrome = left + middle + left[::-1]

            if palindrome > target:
                return palindrome

        # Backtracking:
        # Change the previous position to the next bigger character.
        for i in range(len(ans) - 1, -1, -1):

            # Restore the character currently used at i
            current = ord(ans[i]) - ord('a')
            half[current] += 1

            # Find smallest bigger character
            for c in range(current + 1, 26):
                if half[c] > 0:

                    new_left = ans[:i] + [chr(c + ord('a'))]
                    half[c] -= 1

                    # Fill rest with smallest possible characters
                    for x in range(26):
                        new_left.extend(
                            [chr(x + ord('a'))] * half[x]
                        )

                    left = ''.join(new_left)

                    return left + middle + left[::-1]

        return ""
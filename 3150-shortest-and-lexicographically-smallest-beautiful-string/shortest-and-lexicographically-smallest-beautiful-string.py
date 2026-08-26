from typing import List

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # We have exactly k ones
            while ones == k:
                current = s[left:right + 1]

                # Update answer
                if ans == "" or len(current) < len(ans):
                    ans = current
                elif len(current) == len(ans) and current < ans:
                    ans = current

                # Move left forward
                if s[left] == '1':
                    ones -= 1

                left += 1

        return ans
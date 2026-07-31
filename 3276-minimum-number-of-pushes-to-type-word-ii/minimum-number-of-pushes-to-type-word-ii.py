from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        # Sort frequencies in descending order
        frequencies = sorted(freq.values(), reverse=True)

        ans = 0

        for i, f in enumerate(frequencies):
            ans += f * ((i // 8) + 1)

        return ans
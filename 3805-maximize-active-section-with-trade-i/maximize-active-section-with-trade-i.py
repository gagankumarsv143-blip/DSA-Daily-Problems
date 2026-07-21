class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")

        zero_groups = []
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                zero_groups.append(j - i)
                i = j
            else:
                i += 1

        
        if len(zero_groups) <= 1:
            return ones

        best = 0
        for i in range(len(zero_groups) - 1):
            best = max(best, zero_groups[i] + zero_groups[i + 1])

        return ones + best
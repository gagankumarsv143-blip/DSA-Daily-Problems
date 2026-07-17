class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = how many numbers are divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = number of pairs with gcd exactly d
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            pairs = cnt[d] * (cnt[d] - 1) // 2
            for multiple in range(2 * d, mx + 1, d):
                pairs -= exact[multiple]
            exact[d] = pairs

        # Prefix counts of gcd values
        prefix = []
        gcds = []
        total = 0
        for d in range(1, mx + 1):
            if exact[d]:
                total += exact[d]
                prefix.append(total)
                gcds.append(d)

        # Answer queries using binary search
        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(gcds[idx])

        return ans
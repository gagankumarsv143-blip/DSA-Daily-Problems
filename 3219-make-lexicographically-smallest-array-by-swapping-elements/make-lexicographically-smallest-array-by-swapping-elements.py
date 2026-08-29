from typing import List

class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        n = len(nums)

        # Store (value, original index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = nums[:]

        left = 0

        while left < n:
            right = left

            # Find one connected group
            while right + 1 < n and arr[right + 1][0] - arr[right][0] <= limit:
                right += 1

            # Original indices of this group
            indices = []

            for i in range(left, right + 1):
                indices.append(arr[i][1])

            # Sort indices so smallest values go to earliest positions
            indices.sort()

            # Values are already sorted
            for i in range(right - left + 1):
                ans[indices[i]] = arr[left + i][0]

            left = right + 1

        return ans
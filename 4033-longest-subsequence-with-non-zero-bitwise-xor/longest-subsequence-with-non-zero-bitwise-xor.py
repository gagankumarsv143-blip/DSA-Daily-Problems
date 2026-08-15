class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0

        for num in nums:
            total_xor ^= num

        if total_xor != 0:
            return n
        for num in nums:
            if num != 0:
                return(n - 1)
                break
        else:
            return 0
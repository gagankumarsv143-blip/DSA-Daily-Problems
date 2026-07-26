import math 
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans1 = nums[-1] * nums[-2] * nums[-3]
        ans2 = nums[0] * nums[1] * nums[-1]
        ans = max(ans1,ans2)
        return ans

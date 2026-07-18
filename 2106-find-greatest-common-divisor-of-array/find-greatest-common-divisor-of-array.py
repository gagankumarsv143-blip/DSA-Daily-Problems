from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        num = (gcd(mini,maxi))
        return num


        
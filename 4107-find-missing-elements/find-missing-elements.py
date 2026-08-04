class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        start = min(nums)
        end = max(nums)
        ans = []

        for num in range(start,end+1):
            if num not in s:
                ans.append(num)
        return ans
        
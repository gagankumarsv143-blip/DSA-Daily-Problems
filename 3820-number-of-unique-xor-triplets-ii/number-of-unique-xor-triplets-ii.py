class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        POX = set()

        n = len(nums)

        
        for i in range(n):
            for j in range(i, n):
                POX.add(nums[i] ^ nums[j])

       
        ans = set()

        for x in POX:
            for num in nums:
                ans.add(x ^ num)

        return len(ans)
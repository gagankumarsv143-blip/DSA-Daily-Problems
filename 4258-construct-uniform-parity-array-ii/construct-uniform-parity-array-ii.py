class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = []
        even = []

        for x in nums1:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

        if not odd or not even:
            return True

        if min(odd) < min(even):
            return True

        return False


        
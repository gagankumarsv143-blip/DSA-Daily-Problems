from typing import List

class Solution:
    def maxNumberOfFamilies(self,n: int,reservedSeats: List[List[int]]) -> int:
        rows = {}
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)
        ans = (n - len(rows)) * 2

        for seats in rows.values():
            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            can_left = seats.isdisjoint(left)
            can_middle = seats.isdisjoint(middle)
            can_right = seats.isdisjoint(right)

            if can_left and can_right:
                ans += 2
            elif can_left or can_middle or can_right:
                ans += 1
        return ans
        
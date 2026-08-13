from typing import List

class Solution:
    def longestRepeating(self,s: str,queryCharacters: str,queryIndices: List[int]) -> List[int]:

        n = len(s)

        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc, rc, pre, suf, best, length = a
            lc2, rc2, pre2, suf2, best2, length2 = b

            same = rc == lc2

            new_pre = pre
            new_suf = suf2
            new_best = max(best, best2)

            if same:
                new_best = max(new_best, suf + pre2)

                if pre == length:
                    new_pre = length + pre2

                if suf2 == length2:
                    new_suf = suf + length2

            return [
                lc,
                rc2,
                new_pre,
                new_suf,
                new_best,
                length + length2
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = [
                    s[l],
                    s[l],
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            ans.append(tree[1][4])

        return ans
        
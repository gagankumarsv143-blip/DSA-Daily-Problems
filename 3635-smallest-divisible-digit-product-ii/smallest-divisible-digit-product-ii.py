from typing import Dict

class Solution:
    kFactorCounts = {
        0: {},
        1: {},
        2: {2: 1},
        3: {3: 1},
        4: {2: 2},
        5: {5: 1},
        6: {2: 1, 3: 1},
        7: {7: 1},
        8: {2: 3},
        9: {3: 2},
    }

    def factorize_t(self, t):
        count = {2: 0, 3: 0, 5: 0, 7: 0}

        for p in (2, 3, 5, 7):
            while t % p == 0:
                t //= p
                count[p] += 1

        return count, t == 1

    def subtract(self, a, b):
        res = dict(a)

        for k, v in b.items():
            res[k] = max(0, res.get(k, 0) - v)

        return res

    def get_factor_count(self, count):
        c2 = count.get(2, 0)
        c3 = count.get(3, 0)
        c5 = count.get(5, 0)
        c7 = count.get(7, 0)

        count8, rem2 = divmod(c2, 3)
        count9, count3 = divmod(c3, 2)
        count4, count2 = divmod(rem2, 2)

        count6 = 0

        if count2 == 1 and count3 == 1:
            count2 = 0
            count3 = 0
            count6 = 1

        if count3 == 1 and count4 == 1:
            count2 = 1
            count6 = 1
            count3 = 0
            count4 = 0

        return {
            2: count2,
            3: count3,
            4: count4,
            5: c5,
            6: count6,
            7: c7,
            8: count8,
            9: count9,
        }

    def sum_values(self, d):
        return sum(d.values())

    def construct(self, factors):
        ans = []

        for digit in range(2, 10):
            ans.append(str(digit) * factors.get(digit, 0))

        return "".join(ans)

    def is_subset(self, need, have):
        for p, cnt in need.items():
            if have.get(p, 0) < cnt:
                return False
        return True

    def prime_count_from_string(self, s):
        count = {2: 0, 3: 0, 5: 0, 7: 0}

        for ch in s:
            digit = int(ch)

            for p, f in self.kFactorCounts[digit].items():
                count[p] += f

        return count

    def smallestNumber(self, num: str, t: int) -> str:

        primeCount, ok = self.factorize_t(t)

        if not ok:
            return "-1"

        factorCount = self.get_factor_count(primeCount)

        if self.sum_values(factorCount) > len(num):
            return self.construct(factorCount)

        primeCountPrefix = self.prime_count_from_string(num)

        firstZeroIndex = num.find("0")

        if firstZeroIndex == -1:
            firstZeroIndex = len(num)

            if self.is_subset(primeCount, primeCountPrefix):
                return num

        n = len(num)

        for i in range(n - 1, -1, -1):

            digit = int(num[i])

            primeCountPrefix = self.subtract(
                primeCountPrefix,
                self.kFactorCounts[digit],
            )

            spaceAfter = n - i - 1

            if i > firstZeroIndex:
                continue

            remain = self.subtract(primeCount, primeCountPrefix)

            for biggerDigit in range(digit + 1, 10):

                factorsAfter = self.get_factor_count(
                    self.subtract(
                        remain,
                        self.kFactorCounts[biggerDigit],
                    )
                )

                need = self.sum_values(factorsAfter)

                if need <= spaceAfter:
                    fill = spaceAfter - need

                    return (
                        num[:i]
                        + str(biggerDigit)
                        + "1" * fill
                        + self.construct(factorsAfter)
                    )

        factors = self.get_factor_count(primeCount)

        return (
            "1" * (n + 1 - self.sum_values(factors))
            + self.construct(factors)
        )
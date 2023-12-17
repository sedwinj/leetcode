# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        fraction = n < 0
        n = abs(n)

        def _pow(x: float, n: int) -> float:
            if n == 0:
                return 1

            half_pow = self.myPow(x, n // 2)
            val = half_pow * half_pow
            if n % 2 == 1:
                val *= x

            return val

        val = _pow(x, n)
        return 1 / val if fraction else val

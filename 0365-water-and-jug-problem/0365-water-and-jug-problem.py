class Solution:
    def canMeasureWater(self, x, y, target):
        if target > x + y:
            return False

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return target % gcd(x, y) == 0
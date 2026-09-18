class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0

        is_prime = bytearray(b'\x01') * n
        is_prime[0] = 0
        is_prime[1] = 0

        p = 2

        while p * p < n:
            if is_prime[p]:
                start = p * p
                count = ((n - 1 - start) // p) + 1

                is_prime[start:n:p] = b'\x00' * count

            p += 1

        return sum(is_prime)
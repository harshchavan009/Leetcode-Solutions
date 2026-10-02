class Solution:
    def nthSuperUglyNumber(self, n, primes):
        k = len(primes)

        ugly = [1] * n
        idx = [0] * k
        values = [p for p in primes]

        for i in range(1, n):
            # Find the smallest next possible ugly number
            next_num = values[0]

            for j in range(1, k):
                if values[j] < next_num:
                    next_num = values[j]

            ugly[i] = next_num

            # Move every pointer that produced this number
            for j in range(k):
                if values[j] == next_num:
                    idx[j] += 1
                    values[j] = ugly[idx[j]] * primes[j]

        return ugly[n - 1]
class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total += diff
            tank += diff

            # If we cannot reach the next station,
            # this station cannot be a valid start.
            if tank < 0:
                start = i + 1
                tank = 0

        # If total gas is less than total cost,
        # completing the circuit is impossible.
        if total < 0:
            return -1

        return start
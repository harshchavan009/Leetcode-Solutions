
class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)

        min_price = min(price for factor, price in items)

        # Calculate the value of activating each item
        values = []

        for factor, price in items:
            count = 0

            for other_factor, other_price in items:
                if other_factor % factor == 0:
                    count += 1

            values.append((price, count))

        # 0/1 Knapsack DP
        INF = float('-inf')
        dp = [INF] * (budget + 1)
        dp[0] = 0

        for price, value in values:
            for b in range(budget, price - 1, -1):
                if dp[b - price] != INF:
                    dp[b] = max(
                        dp[b],
                        dp[b - price] + value
                    )

        # Spend remaining budget on cheapest items
        ans = 0

        for spent in range(budget + 1):
            if dp[spent] != INF:
                extra = (budget - spent) // min_price
                ans = max(ans, dp[spent] + extra)

        return ans

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        hold = -prices[0]
        sold = 0
        cooldown = 0

        for i in range(1, len(prices)):
            prev_hold = hold
            prev_sold = sold
            prev_cooldown = cooldown

            # Buy today or keep holding
            hold = max(prev_hold, prev_cooldown - prices[i])

            # Sell today
            sold = prev_hold + prices[i]

            # Stay in cooldown / stay without stock
            cooldown = max(prev_cooldown, prev_sold)

        return max(sold, cooldown)
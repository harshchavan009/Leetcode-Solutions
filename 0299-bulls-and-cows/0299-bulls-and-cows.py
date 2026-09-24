class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        count_secret = [0] * 10
        count_guess = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                count_secret[int(s)] += 1
                count_guess[int(g)] += 1

        cows = 0

        for d in range(10):
            cows += min(count_secret[d], count_guess[d])

        return str(bulls) + "A" + str(cows) + "B"
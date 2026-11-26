
class Solution:
    def canAliceWin(self, n):
        stones = 10
        moves = 0

        while n >= stones:
            n -= stones
            moves += 1
            stones -= 1

        return moves % 2 == 1

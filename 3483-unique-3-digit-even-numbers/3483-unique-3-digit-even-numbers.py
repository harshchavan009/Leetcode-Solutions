class Solution:
    def totalNumbers(self, digits):
        count = [0] * 10

        for d in digits:
            count[d] += 1

        answer = 0

        for a in range(1, 10):          # Hundreds digit: cannot be 0
            for b in range(10):         # Tens digit
                for c in range(0, 10, 2):  # Units digit: must be even
                    # Need enough copies of each digit
                    if a == b == c:
                        if count[a] >= 3:
                            answer += 1
                    elif a == b:
                        if count[a] >= 2 and count[c] >= 1:
                            answer += 1
                    elif a == c:
                        if count[a] >= 2 and count[b] >= 1:
                            answer += 1
                    elif b == c:
                        if count[b] >= 2 and count[a] >= 1:
                            answer += 1
                    else:
                        if count[a] >= 1 and count[b] >= 1 and count[c] >= 1:
                            answer += 1

        return answer
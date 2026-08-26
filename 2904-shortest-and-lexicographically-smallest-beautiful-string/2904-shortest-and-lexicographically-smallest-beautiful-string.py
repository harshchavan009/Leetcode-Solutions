class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        left = 0
        ones = 0
        min_len = n + 1
        answer = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Shrink the window while it still contains at least k ones
            while left <= right and ones >= k:
                if ones == k:
                    current_len = right - left + 1
                    current = s[left:right + 1]

                    if current_len < min_len:
                        min_len = current_len
                        answer = current
                    elif current_len == min_len and (answer == "" or current < answer):
                        answer = current

                # Move left forward
                if s[left] == '1':
                    ones -= 1
                left += 1

        return answer
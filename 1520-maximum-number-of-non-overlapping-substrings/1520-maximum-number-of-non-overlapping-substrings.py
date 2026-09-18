class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Build the smallest valid interval for each character
        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                # This character appears before our left boundary,
                # so the substring cannot be valid.
                if first[x] < left:
                    valid = False
                    break

                # Need to include all occurrences of this character
                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((left, right))

        # Earliest ending interval first.
        # For the same end, prefer the shorter interval.
        intervals.sort(key=lambda x: (x[1], -x[0]))

        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result
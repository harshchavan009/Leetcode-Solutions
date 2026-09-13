class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(index, parts):
            # If we have 4 parts, all digits must be used
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            # Remaining digits must be enough for the remaining parts
            remaining = len(s) - index
            parts_left = 4 - len(parts)

            if remaining < parts_left or remaining > parts_left * 3:
                return

            # Try taking 1, 2, or 3 digits
            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                # No leading zeros unless the part is exactly "0"
                if length > 1 and part[0] == '0':
                    continue

                # Value must be between 0 and 255
                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(index + length, parts)
                parts.pop()

        backtrack(0, [])

        return result
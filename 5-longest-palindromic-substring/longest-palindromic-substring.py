class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start = 0
        max_len = 1

        for i in range(n):
            # Stop early if remaining characters cannot beat max_len
            if n - i <= max_len // 2:
                break

            # Skip duplicate characters to handle odd & even centers at once
            left = right = i
            while right < n - 1 and s[right] == s[right + 1]:
                right += 1

            # Expand outward around the core of duplicates
            while left > 0 and right < n - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1

            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                start = left

        return s[start:start + max_len]
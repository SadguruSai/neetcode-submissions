class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            # Odd-length palindromes
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

            # Even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans
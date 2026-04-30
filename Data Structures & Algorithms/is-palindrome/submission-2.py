class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for c in range(len(s)):
            if s[c].isalnum():
                result += s[c].lower()
        return result == result[::-1]
        
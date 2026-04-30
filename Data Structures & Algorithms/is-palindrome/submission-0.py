class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for c in range(len(s)):
            if s[c].isalnum():
                result += s[c].lower()
        start = 0
        end = len(result) - 1
        while start <= end:
            if result[start] != result[end]:
                return False
            start += 1
            end -= 1
        return True
        
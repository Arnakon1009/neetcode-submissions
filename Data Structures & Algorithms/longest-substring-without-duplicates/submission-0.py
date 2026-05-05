class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen and r < len(s) and l < len(s):
                seen.discard(s[l])
                l += 1

            w = (r-l) + 1
            res = max(w, res)

            seen.add(s[r])
        return res
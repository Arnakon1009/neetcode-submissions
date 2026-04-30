class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        f = Counter(s)
        f2 = Counter(t)

        if f == f2:
            return True
        return False
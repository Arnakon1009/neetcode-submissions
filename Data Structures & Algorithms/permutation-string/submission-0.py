class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        F1 = Counter(s1)
        l = 0
        r = len(s1) - 1
        for i in range(len(s2)):
            if r < len(s2):
                data = s2[l:r+1]
                F2 = Counter(data)
                if F1 == F2:
                    return True
                else:
                    l += 1
                    r += 1
        return False
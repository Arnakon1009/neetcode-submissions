class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            length = 0
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res

            


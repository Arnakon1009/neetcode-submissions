class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter, defaultdict
        data = defaultdict(list)
        res = []
        for i in strs: 
            sorted_text = "".join(sorted(i))
            data[sorted_text].append(i)
        for i, j in data.items():
            res.append(j)
        return res